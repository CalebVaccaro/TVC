import qwiic_titan_gps
import pynmea2
import sys
from time import sleep
import json
import struct
import ast

class XGPS:

    gps = None

    def getSensor():

        qwiicGPS = qwiic_titan_gps.QwiicTitanGps()

        if qwiicGPS.connected is False:
            print("GPS-XA110 Not Found", file=sys.stderr)
            sys.exit(0)
            return None

        qwiicGPS.begin()
        XGPS.gps = qwiicGPS
        print("GPS-XA110 Is Communicating")
        return qwiicGPS

    def getRawData():
        gps = XGPS.gps
        #while True:
        if gps.get_nmea_data() is True:
            return json.dumps(gps.gnss_messages, sort_keys=True, default=str)
 
#if __name__ == 'XGPS':
    #try:
        #GPS = getSensor()
        #getLatLong(getRawData())
    #except (KeyboardInterrupt, SystemExit) as exErr:
        #print("Ending GPS Data")