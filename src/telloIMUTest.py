import cv2, math, time, serial, json, numpy as np
from djitellopy import Tello
from time import sleep
from fusion import Fusion
from threading import Thread

import time
import board
import busio
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER,
    BNO_REPORT_ROTATION_VECTOR,
)
from adafruit_bno08x.i2c import BNO08X_I2C

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
bno = BNO08X_I2C(i2c)

bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
#bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)

CAN_USE_IMU = True
IMU_ERROR_MESSAGE = 'IMU connection could not be established, does your machine have one plugged in?'\

# If we can't use the IMU, error handle
try:
    from icm20948 import ICM20948
except:
    CAN_USE_IMU = False

def startTello():
    tello = Tello()
    tello.connect()
    return tello
    return True

def stopTello():
    tello.send_rc_control(0, 0, 0, 0)
    tello.land()
    keepRecording = False
    recorder.join()
    tello.end()
    return True
    
def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video1.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()
    
def getIMUData(imu):
    #mx, my, mz = imu.read_magnetometer_data()
    mx, my, mz = bno.magnetic
    #ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
    ax, ay, az = bno.acceleration
    gx, gy, gz = bno.gyro

    #outFusion = Fusion.update(imu,(ax, ay, az),(gx, gy, gz),(mx, my, mz))
    # pass true or false to perform logging
    return getIMUFusion((ay,ax,az),(gy,gx,gz),(my,mx,mz))

def getIMUFusion(a,g,m):
    GYRO_SENS = 65.536 # Each IMU has a specific sensitivity factor that you need to scale raw data into deg/s
    ACCEL_SENS = 1 # I changed some settings on my openlog board, but normally I would need a scaling factor for the accelerometer as well
    pitch = 0
    roll = 0
    last_time = time.time()
    accel = a
    gyro = g
    magn = m
    
    # Integrating gyroscope data
    dt = time.time() - last_time
    last_time = time.time()
    pitch += (gyro[0]/GYRO_SENS)*dt
    roll -= (gyro[1]/GYRO_SENS)*dt

    # Only use accelerometer when it's steady (magnitude is near 1g)
    forceMagnitude = math.sqrt(accel[0]**2 + accel[1]**2 + accel[2]**2)
    if forceMagnitude > 0.9 and forceMagnitude < 1.1:
        pitch = pitch*0.95 + math.atan2(accel[1], math.sqrt(accel[0]**2 + accel[2]**2) )*180/math.pi *0.05
        roll = roll*0.9 + math.atan2(-accel[0], accel[2])*180/math.pi *0.05
    
    p = (pitch*180/math.pi)
    r = (roll*180/math.pi)
    return (p,r)
    
def moveTelloWithIMU(pitch, roll):
    uD = 0
    lR = 0
    
    #up-down currently: INVERTED
    if pitch < 0 and pitch > -51:
        # go down a bit
        uD = 25
    elif pitch <= -51:
        # go down a lot
        uD = 50
    elif pitch > 0 and pitch < 51:
        # go up a bit
        uD = -25
    elif pitch >= 51:
        # go up a lot
        uD = -50
    else:
        uD = 0
        
    #left-right
    if roll < 0 and roll > -51:
        # go left a bit
        lR = -25
    elif roll <= -51:
        # go left a lot
        lR = -75
    elif roll > 0 and roll < 51:
        # go right a bit
        lR = 25
    elif roll >= 51:
        # go right a lot
        lR = 75
    else:
        lR = 0
    
    print(pitch , roll)
    tello.send_rc_control(int(lR/2.5),20,uD,lR)

# INIT PROGRAM
# start Tello
tello = startTello()

# start recording
keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()
recorder = Thread(target=videoRecorder)
recorder.start()

imu = ICM20948()
tello.takeoff()
tello.move_up(30)
sleep(3)

while True:
    # check if IMU is Null
    if imu is None:
        break
    
    # Tello x IMU
    try:
        p,r = getIMUData(imu)
        moveTelloWithIMU(p,r)
    except:
        print("couldnt read IMU/Tello Data")
    
    # cv2 Get Img from Frame and Display
    img = frame_read.frame
    cv2.imshow("drone", img)
    
    # get cv2 Key
    key = cv2.waitKey(1) & 0xff
    
    # escape Program
    if key == 27: # ESC
        stopTello()
        break

stopTello()
exit()
