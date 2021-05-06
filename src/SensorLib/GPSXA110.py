import qwiic_titan_gps
import pynmea2
import sys
from time import sleep

def getSensor():

    qwiicGPS = qwiic_titan_gps.QwiicTitanGps()

    if qwiicGPS.connected is False:
        print("GPS-XA110 Not Found", file=sys.stderr)
        sys.exit(0)
        return

    qwiicGPS.begin()
    print("GPS-XA110 Is Communicating", file=sys.stderr)
    return qwiicGPS

def getRawData():
    while True:
        if GPS.get_nmea_data() is True:
            getLatLong(GPS.gnss_messages)
        sleep(1)
        
def getLatLong(rawData):
     print("Latitude: {}, Longitude: {}, Time: {}".format(
                rawData['Latitude'],
                rawData['Longitude'],
                rawData['Time']))
                
if __name__ == '__main__':
    try:
        GPS = getSensor()
        getLatLong(getRawData())
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending Basic Example.")
        sys.exit(0)