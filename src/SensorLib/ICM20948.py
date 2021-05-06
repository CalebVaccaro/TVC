from __future__ import print_function
import qwiic_icm20948
import time
import sys
from fusion import Fusion

def getSensor():

    imu20948 = qwiic_icm20948.QwiicIcm20948()

    if imu20948.connected == False:
        print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    imu20948.begin()
    print("IMU-20948 Is Communicating", file=sys.stderr)
    return imu20948

def getRawData():
    while True:
            if IMU.dataReady():
                IMU.getAgmt()
                return getFusionData(((IMU.axRaw,IMU.ayRaw,IMU.azRaw)
                                 ,(IMU.gxRaw,IMU.gyRaw,IMU.gzRaw)
                                 ,(IMU.mxRaw,IMU.myRaw,IMU.mzRaw)))
            else:
                print("Waiting for data")
                time.sleep(0.5)
                return (0,0,0)
            sleep(1)
        
def getFusionData(rawData):
    print(rawData[2])
    Fusion.update((rawData[0][0],rawData[0][1],rawData[0][2]),(rawData[1][0],rawData[1][1],rawData[1][2]),(rawData[2][0],rawData[2][1],rawData[2][2]))
    print(Fusion.pitch)
                
if __name__ == '__main__':
    try:
        IMU = getSensor()
        getFusionData(getRawData())
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending Basic Example.")
        sys.exit(0)