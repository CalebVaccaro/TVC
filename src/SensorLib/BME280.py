import qwiic_bme280
import time
import sys

class BME_280:
    
    def getSensor():
        mySensor = qwiic_bme280.QwiicBme280()

        if mySensor.connected == False:
            print("The Qwiic BME280 device isn't connected to the system.", \
                file=sys.stderr)
            return

        mySensor.begin()
        print("IMU-20948 Is Communicating", file=sys.stderr)
        return mySensor

    def getRawData(BME):
        return str(str(BME.humidity)
                + str(BME.pressure)
                + str(BME.altitude_meters)
                + str(BME.temperature_fahrenheit - 10)).encode()

#if __name__ == '__main__':
	#try:
		#runExample()
	#except (KeyboardInterrupt, SystemExit) as exErr:
		#print("\nEnding Example 1")
		#sys.exit(0)