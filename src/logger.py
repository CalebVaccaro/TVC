import json
from datetime import datetime
from SensorLib.GPSXA110 import XGPS
from SensorLib.BME280 import BME_280
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.IMUBNO0802 import BNO2_IMU

class Logger():
    log = False
    file = None
    
    def LogLurk():
        Logger.log = True
        Logger.file = open("log/log.json","a")
    
    def LogInfo():
        while(Logger.log):
            try:
                dataString = {
                        "icm209" : str(ICM_IMU.getRawData()),
                        "bno1" : str(BNO_IMU.getRawData()),
                        "bno2" : str(BNO2_IMU.getRawData()),
                        "xa110" : str(XGPS.getRawData()),
                        "bme280" : str(BME_280.getRawData())
                    }
                jsonData = json.dumps(dataString)
                Logger.file.write(jsonData+str(",\n"))
            except:
                print("invalid data")

        Logger.file.write("\n")
        Logger.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
        Logger.file.close()
