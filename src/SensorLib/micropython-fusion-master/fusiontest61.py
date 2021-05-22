# fusiontest6.py Simple test program for 6DOF sensor fusion on Pyboard
# Author Peter Hinch
# Released under the MIT License (MIT)
# Copyright (c) 2017 Peter Hinch
# V0.8 14th May 2017 Option for external switch for cal test. Make platform independent.
# V0.7 25th June 2015 Adapted for new MPU9x50 interface

from fusion import Fusion
import qwiic_icm20948
import sys
import utime as time

def getSensor():

    imu20948 = qwiic_icm20948.QwiicIcm20948()

    if imu20948.connected == False:
        print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    imu20948.begin()
    print("IMU-20948 Is Communicating", file=sys.stderr)
    return imu20948

IMU = getSensor()
fuse = Fusion()

# Choose test to run
Timing = True

if Timing:
    IMU.getAgmt()
    accel = (IMU.axRaw,IMU.ayRaw,IMU.azRaw)
    gyro = (IMU.gxRaw,IMU.gyRaw,IMU.gzRaw)
    start = time.ticks_us()  # Measure computation time only
    fuse.update_nomag(accel, gyro) # 979μs on Pyboard
    t = time.ticks_diff(time.ticks_us(), start)
    print("Update time (uS):", t)

while True:
    IMU.getAgmt()
    fuse.update_nomag((IMU.axRaw,IMU.ayRaw,IMU.azRaw), (IMU.gxRaw,IMU.gyRaw,IMU.gzRaw))
    print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(fuse.heading, fuse.pitch, fuse.roll))
    time.sleep(1)
