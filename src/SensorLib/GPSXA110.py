import qwiic_titan_gps
import pynmea2
import sys
from time import sleep
import json
import struct
import ast

class XGPS:

    def getSensor():

        qwiicGPS = qwiic_titan_gps.QwiicTitanGps()

        if qwiicGPS.connected is False:
            print("GPS-XA110 Not Found", file=sys.stderr)
            sys.exit(0)
            return None

        qwiicGPS.begin()
        print("GPS-XA110 Is Communicating", file=sys.stderr)
        return qwiicGPS

    def getRawData(GPS):
        while True:
            if GPS.get_nmea_data() is True:
                return XGPS.getLatLong(GPS.gnss_messages)
            
    def getLatLong(rawData):
        return json.dumps(rawData, sort_keys=True, default=str)
     
#if __name__ == 'XGPS':
    #try:
        #GPS = getSensor()
        #getLatLong(getRawData())
    #except (KeyboardInterrupt, SystemExit) as exErr:
        #print("Ending GPS Data")