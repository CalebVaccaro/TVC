import qwiic_bme280
import time
import sys

class BME_280:
    
    bme = None
    
    def getSensor():
        sensor = qwiic_bme280.QwiicBme280()

        if sensor.connected == False:
            print("The Qwiic BME280 device isn't connected to the system.", \
                file=sys.stderr)
            sys.exit(0)
            return

        sensor.begin()
        BME_280.bme = sensor
        print("BME-280 Is Communicating")
        return sensor

    def getRawData():
        bme = BME_280.bme
        return str("Humitidy"+str(bme.humidity)
                + " , Pressure"+str(bme.pressure)
                + " , Altitude"+str(bme.altitude_meters)
                + " , Temperature"+str(bme.temperature_fahrenheit - 10))

#if __name__ == '__main__':
	#try:
		#runExample()
	#except (KeyboardInterrupt, SystemExit) as exErr:
		#print("\nEnding Example 1")
		#sys.exit(0)