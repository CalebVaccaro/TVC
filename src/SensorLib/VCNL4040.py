#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qwiic_proximity_ex1.py
#
# Simple Example for the Qwiic Proximity Device
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2019
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 1
#
# - Setup the device
# - Output the proximity value

from __future__ import print_function
import qwiic_proximity
import time
import sys

class VCNL_4040:

    prox = None
    def getSensor():
        oProx = qwiic_proximity.QwiicProximity()

        if oProx.connected == False:
            print("VCNL40 is Not Connected", \
                file=sys.stderr)
            return

        oProx.begin()
        VCNL_4040.prox = oProx
        print("VCNL40 is Connected")
        return oProx
        #print(oProx.get_id())

    def getRawData():
        #while True:
            #print("Proximity Value: %d" % proxValue)
        #time.sleep(.4)
        return VCNL_4040.prox.get_proximity()


#if __name__ == '__main__':
	#try:
		#runExample()
	#except (KeyboardInterrupt, SystemExit) as exErr:
		#print("\nEnding Example 1")
		#sys.exit(0)



