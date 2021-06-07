from __future__ import print_function
import qwiic_micro_oled
import sys

class O_LED:
    
    screen = None
    def getSensor():
        myOLED = qwiic_micro_oled.QwiicMicroOled()

        if not myOLED.connected:
            print("OLED is Not Connected", \
                file=sys.stderr)
            return
        
        myOLED.set_font_type(1) 
        myOLED.begin()
        O_LED.screen = myOLED
        print("OLED is Connected")
        O_LED.setText("OLED CONNECTED")
        return O_LED.screen

    def setText(text):
        O_LED.screen.clear(O_LED.screen.ALL)  #  Clear the display's memory (gets rid of artifacts)
        O_LED.screen.set_cursor(0, 0) # Set cursor to top-left
        O_LED.screen.print(text) 
        O_LED.screen.display()
        
    def setBMP(bmp):
        O_LED.screen.clear(OLED.screen.PAGE)  #  Clear the display's memory (gets rid of artifacts)
        O_LED.screen.draw_bitmap(bmp)
        O_LED.screen.display()

# if __name__ == '__main__':
#     try:
#         runExample()
#     except (KeyboardInterrupt, SystemExit) as exErr:
#         print("\nEnding OLED Hello Example")
#         sys.exit(0)