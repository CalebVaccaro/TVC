import time
import board
import busio
import sys
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER,
    #BNO_REPORT_RAW_ACCELEROMETER,
    #BNO_REPORT_RAW_GYROSCOPE,
    #BNO_REPORT_RAW_MAGNETOMETER
)
from SensorLib.BNO0802.adafruit_bno08x.i2c import BNO08X2_I2C
from SensorLib.IMUFusion import Fusion
import json

class BNO2_IMU:
    
    imu = None

    def getSensor():
        i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
        bno = BNO08X2_I2C(i2c)

        if bno is None:
            print("IMU-BNO0802 Not Found", file=sys.stderr)
            sys.exit(0)
            return None

        bno.enable_feature(BNO_REPORT_ACCELEROMETER)
        bno.enable_feature(BNO_REPORT_GYROSCOPE)
        bno.enable_feature(BNO_REPORT_MAGNETOMETER)
        #bno.enable_feature(BNO_REPORT_RAW_ACCELEROMETER)
        #bno.enable_feature(BNO_REPORT_RAW_GYROSCOPE)
        #bno.enable_feature(BNO_REPORT_RAW_MAGNETOMETER)
        BNO2_IMU.imu = bno
        print("IMU-BNO0802 Is Communicating")
        return bno

    def getFusionData():
        bno = BNO2_IMU.imu
        if bno._data_ready is False:
            return BNO2_IMU.getRefinedData((0,0))
        try:
            ax, ay, az = bno.acceleration
            gx, gy, gz = bno.gyro
            mx, my, mz = bno.magnetic
            string = json.dumps(Fusion.calFusion((ay,ax,az),(gy,gx,gz),(my,mx,mz)))
            return string
        except:
            return BNO2_IMU.getRefinedData((0,0))

    def getRawData():
        bno = BNO2_IMU.imu
        if bno._data_ready is False:
            return BNO2_IMU.getRefinedData((0,0,0))
        try:
            #if bno._data_ready is False:
                #return BNO2_IMU.getRefinedData((0,0,0))
            ax, ay, az = bno.acceleration
            gx, gy, gz = bno.gyro
            mx, my, mz = bno.magnetic
            string = json.dumps(((ay,ax,az),(gy,gx,gz),(my,mx,mz)), sort_keys=True, default=str)
            return string
        except:
            return BNO2_IMU.getRefinedData((0,0,0))
        
    def getRefinedData(rawData):
        return json.dumps(rawData)
    
#if __name__ == '__main__':  
    #while True:
        #try:
            #print(getRawData())
            #time.sleep(.21)
        #except (KeyboardInterrupt, SystemExit) as exErr:
            #print("no data")