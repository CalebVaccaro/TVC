from __future__ import print_function
import qwiic_icm20948
import time
import utime
import sys
import json
from SensorLib.IMUFusion import Fusion

class ICM_IMU:
    
    imu = None

    def getSensor():

        imu20948 = qwiic_icm20948.QwiicIcm20948()

        if imu20948.connected == False:
            print("The Qwiic ICM20948 device isn't connected to the system.", file=sys.stderr)
            return

        imu20948.begin()
        ICM_IMU.imu = imu20948
        print("IMU-20948 Is Communicating", file=sys.stderr)
        return imu20948

    def getFusionData(IMU):
        if IMU.dataReady():
            IMU.getAgmt()
            mx, my, mz = (IMU.mxRaw,IMU.myRaw,IMU.mzRaw)
            ax, ay, az = (IMU.axRaw,IMU.ayRaw,IMU.azRaw)
            gx, gy, gz = (IMU.gxRaw,IMU.gyRaw,IMU.gzRaw)
            string = json.dumps(Fusion.getIMUFusion((ay,ax,az),(gy,gx,gz),(my,mx,mz)))
            return string
        else:
            string = json.dumps((0,0))
            return string

    def getRawData(IMU):
        if IMU.dataReady():
            IMU.getAgmt()
            mx, my, mz = (IMU.mxRaw,IMU.myRaw,IMU.mzRaw)
            ax, ay, az = (IMU.axRaw,IMU.ayRaw,IMU.azRaw)
            gx, gy, gz = (IMU.gxRaw,IMU.gyRaw,IMU.gzRaw)
            string = json.dumps(((ay,ax,az),(gy,gx,gz),(my,mx,mz)), sort_keys=True, default=str)
            return string
        else:
            string = json.dumps((0,0,0))
            return string

#if __name__ == '__main__':
    #IMU = ICM_IMU.getSensor()
    #while True:
        #try: 
            #print(ICM_IMU.getRawData())
        #except (KeyboardInterrupt, SystemExit) as exErr:
            #print("no data")
