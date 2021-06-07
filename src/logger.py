import json
from datetime import datetime
from SensorLib.GPSXA110 import XGPS
from SensorLib.BME280 import BME_280
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.IMUBNO0802 import BNO2_IMU
from SensorLib.Camera import Camera
from SensorLib.VCNL4040 import VCNL_4040
from SensorLib.Button import SFButton
from SensorLib.OLED import O_LED
from time import sleep

class Logger():
    log = False
    file = None
    
    def LogLurk():
        Logger.log = True
        Logger.file = open("log/log.json","a")
        
    def StopLog():
        Logger.log = False
        Camera.stopRecording()
        print("stop logging")
    
    def LogVisuals():
        Camera.startRecording()
    
    counter = 0
    def LogInfo():
        while(Logger.counter < 100):
            OLEDdata = str(BNO2_IMU.getRawData())
            #try:
            dataString = {
                "icm209" : str(ICM_IMU.getRawData()),
                "bno1" : str(BNO_IMU.getRawData()),
                "bno2" : OLEDdata,
                "xa110" : str(XGPS.getRawData()),
                "bme280" : str(BME_280.getRawData()),
                "vcnl40" : str(VCNL_4040.getRawData()),
                "button" : str(SFButton.getRawData())
            }
            jsonData = json.dumps(dataString)
            Logger.file.write(jsonData+str("\n"))
            Logger.counter += 1
            #O_LED.setText(OLEDdata)
            print(Logger.counter)
            sleep(.02)
            #except:
                #print("invalid data")

        Logger.file.write("\n")
        Logger.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"\n")
        Logger.file.close()
        Logger.StopLog()
