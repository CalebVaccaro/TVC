from __future__ import print_function
from SensorLib.Qwiic_Button import qwiic_button 
import time
import sys

class SFButton:
    
    button = None
    def getSensor():
        my_button = qwiic_button.QwiicButton()

        if my_button.begin() == False:
            print("SFButton is Not Connected", \
                file=sys.stderr)
            return
        
        SFButton.button = my_button;
        print("SFButton is Connected")
        return SFButton.button;
        
    def getRawData():
        #while True:
        #time.sleep(0.02)
        if SFButton.button.is_button_pressed() == True:
            return print("\nThe button is pressed!")
        else:    
            return print("\nThe button is not pressed!")

#if __name__ == '__main__':
    #try:
        #run_example()
    #except (KeyboardInterrupt, SystemExit) as exErr:
        #print("\nEnding Example 1")
        #sys.exit(0)

