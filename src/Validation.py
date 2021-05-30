from SensorLib.GPSXA110 import XGPS
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.IMUBNO0802 import BNO_IMU
from SensorLib.BME280 import BME_280
from SensorLib.TVCMount import Servos
from time import sleep

def ValidateSensors():
    # Get Sensors
    GPS = XGPS.getSensor()
    print("GPS Validated")
    sleep(.5)
    IMU209 = ICM_IMU.getSensor()
    sleep(.5)
    IMU080 = BNO_IMU.getSensor()
    sleep(.5)
    IMU0802 = BNO_IMU.getSensor()
    print("IMUs Validated")
    sleep(.5)
    print("Sensors Validated")

def ValidateTVCMount(cont):
    sleep(2)
    print("...Moving Motors...")
    if cont is True:
        Servos.TestServosContinuous()
    else:
        Servos.TestServos()
    print("end servo testing")

def ValidateBattery():
    print("RPI is ON")

