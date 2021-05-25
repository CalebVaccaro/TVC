from SensorLib.GPSXA110 import XGPS
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.BME280 import BME_280
from SensorLib.TVCMount import Servos
from time import sleep

def ValidateSensors():
    # Get Sensors
    GPS = XGPS.getSensor()
    print("GPS Validated")
    IMU209 = ICM_IMU.getSensor()
    IMU080 = BNO_IMU.getSensor()
    print("IMUs Validated")
    print("Sensors Validated")

def ValidateTVCMount():
    sleep(2)
    print("...Moving Motors...")
    Servos.TestServos()
    print("end servo testing")

def ValidateBattery():
    print("RPI is ON")

