from SensorLib.GPSXA110 import XGPS
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.IMUBNO0802 import BNO2_IMU
from SensorLib.BME280 import BME_280
from SensorLib.TVCMount import Servos
from SensorLib.Camera import Camera
from SensorLib.VCNL4040 import VCNL_4040
from SensorLib.Button import SFButton
from SensorLib.OLED import O_LED
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
    sleep(.5)
    VCNL40 = VCNL_4040.getSensor()
    sleep(.5)
    oLED = O_LED.getSensor()
    print("Env Sensors Validated", file=sys.stderr)
    sleep(.5)
    PiCam = Camera.getSensor()
    print("Camera Validated", file=sys.stderr)
    sleep(.5)
    Button = SFButton.getSensor()
    print("Input Sensor Validated", file=sys.stderr)
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

