import socket
from SensorLib.GPSXA110 import XGPS
from SensorLib.ICM20948 import ICM_IMU
from SensorLib.IMUBNO080 import BNO_IMU
from SensorLib.BME280 import BME_280
from time import sleep

IP = "192.168.1.3"
Port = 699

# Create UDP Socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Get Sensors
GPS = XGPS.getSensor()
IMU209 = ICM_IMU.getSensor()
IMU080 = BNO_IMU.getSensor()
#BME280 = BME_280.getSensor()

print("All Started Sensors...")
print("Sending Sensor Data")
 
# Send Data Loop

while(True):
    jsonData = {
        "GPS" : XGPS.getLatLong(XGPS.getRawData(GPS)),
        "IMU1" : ICM_IMU.getFusionData(IMU209),
        "IMU2" : BNO_IMU.getFusionData(IMU080)
    }
    message = str(jsonData).encode()
    #+ BME_280.getRawData(BME280)).encode()
    #print(message)
    sock.sendto(message, (IP, Port))
    
    
    