from SensorLib.GPSXA110 import XGPS
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.IMUBNO0802 import BNO2_IMU
from SensorLib.BME280 import BME_280
from SensorLib.TVCMount import Servos
from time import sleep
import sys

def ValidateSensors():
    print("Validating Sensors...", file=sys.stderr)
    # Get Sensors
    GPS = XGPS.getSensor()
    print("GPS Validated", file=sys.stderr)
    sleep(.5)
    IMU209 = ICM_IMU.getSensor()
    sleep(.5)
    IMU080 = BNO_IMU.getSensor()
    sleep(.5)
    IMU0802 = BNO2_IMU.getSensor()
    print("IMUs Validated", file=sys.stderr)
    sleep(.5)
    BME280 = BME_280.getSensor()
    print("Env Sensors Validated", file=sys.stderr)
    print("Sensors Validated", file=sys.stderr)

def ValidateTVCMount(cont):
    sleep(2)
    print("...Testing Servos...")
    if cont is True:
        Servos.TestServosContinuous()
    else:
        Servos.TestServos()
    print("End Servo Testing")

def ValidateBattery():
    print("RPI is ON", file=sys.stderr)

