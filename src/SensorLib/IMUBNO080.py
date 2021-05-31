import time
import board
import busio
import sys
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_MAGNETOMETER
)
from adafruit_bno08x.i2c import BNO08X_I2C
from SensorLib.IMUFusion import Fusion
import json

class BNO_IMU:
    
    imu = None

    def getSensor():
        i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
        bno = BNO08X_I2C(i2c)

        if bno is None:
            print("IMU-BNO080 Not Found", file=sys.stderr)
            sys.exit(0)
            return None

        bno.enable_feature(BNO_REPORT_ACCELEROMETER)
        bno.enable_feature(BNO_REPORT_GYROSCOPE)
        bno.enable_feature(BNO_REPORT_MAGNETOMETER)
        BNO_IMU.imu = bno
        print("IMU-BNO080 Is Communicating")
        return bno

    def getFusionData():
        bno = BNO_IMU.imu
        if bno.acceleration is None:
            return BNO_IMU.getRefinedData((0,0))
        try:
            if bno.acceleration is None:
                return BNO_IMU.getRefinedData((0,0))
            ax, ay, az = bno.acceleration
            gx, gy, gz = bno.gyro
            mx, my, mz = bno.magnetic
            string = json.dumps(Fusion.getIMUFusion((ay,ax,az),(gy,gx,gz),(my,mx,mz)))
            return string
        except:
            return BNO_IMU.getRefinedData((0,0))

    def getRawData():
        bno = BNO_IMU.imu
        print(bno._data_ready)
        if bno._data_ready is False:
            return BNO_IMU.getRefinedData((0,0,0))
        try:
            if bno._data_ready is False:
                return BNO_IMU.getRefinedData((0,0,0))
            ax, ay, az = bno.acceleration
            gx, gy, gz = bno.gyro
            mx, my, mz = bno.magnetic
            string = json.dumps(((ay,ax,az),(gy,gx,gz),(my,mx,mz)), sort_keys=True, default=str)
            return string
        except:
            return BNO_IMU.getRefinedData((0,0,0))
        
    def getRefinedData(rawData):
        return json.dumps(rawData)
    
#if __name__ == '__main__':  
    #while True:
        #try:
            #print(getRawData())
            #time.sleep(.21)
        #except (KeyboardInterrupt, SystemExit) as exErr:
            #print("no data")