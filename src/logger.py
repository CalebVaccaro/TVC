from datetime import datetime
from SensorLib.ICM20948 import ICM_IMU
import json

class Logger():
    log = False
    file = None
    
    def LogLurk():
        Logger.log = True
        Logger.file = open("log.json","a")
    
    def LogInfo():
        while(Logger.log):
            if ICM_IMU.imu.dataReady():
                ICM_IMU.imu.getAgmt()
                mx, my, mz = (ICM_IMU.imu.mxRaw,ICM_IMU.imu.myRaw,ICM_IMU.imu.mzRaw)
                ax, ay, az = (ICM_IMU.imu.axRaw,ICM_IMU.imu.ayRaw,ICM_IMU.imu.azRaw)
                gx, gy, gz = (ICM_IMU.imu.gxRaw,ICM_IMU.imu.gyRaw,ICM_IMU.imu.gzRaw)
                string = {
                    "icm209" : str(((ay,ax,az),(gy,gx,gz),(my,mx,mz)))
                }
                jsonData = json.dumps(string)
                Logger.file.write(jsonData)

        Logger.file.write("\n")
        Logger.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
        Logger.file.close()
