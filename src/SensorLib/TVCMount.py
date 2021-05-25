from pi_servo_hat import PiServoHat
import time

class Servos():
    
    def TestServos():
        
        # Initialize Constructor
        test = PiServoHat()
        
        # Restart Servo Hat (in case Hat is frozen/locked)
        test.restart()
        
        # Test Run
        #########################################
        # Moves servo position to 0 degrees (1ms), Channel 0
        test.move_servo_position(0, 0)

        # Moves servo position to 90 degrees (2ms), Channel 0
        test.move_servo_position(1, 45)
        
    def TestServosContinuous():
        
        # Restart Servo Hat (in case Hat is frozen/locked)
        test.restart()
        
        # Test Run
        #########################################
        # Moves servo position to 0 degrees (1ms), Channel 0
        test.move_servo_position(0, 0)

        # Pause 1 sec
        time.sleep (1)
        
        loop = 100
        # Sweep
        #########################################
        while loop > 0:
            for i in range(0, 45):
                print(i)
                test.move_servo_position(0, i)
                time.sleep(.005)
            for i in range(45, 0, -1):
                print(i)
                test.move_servo_position(1, i)
                time.sleep(.005)
            loop = loop - 1


#########################################
# Code below may damage servo, use with caution
# Test sweep for full range of servo (outside 0 to 180 degrees).
# while True:
#     for i in range(-23, 100):
#         print(i)
#         test.move_servo_position(0, i)
#         time.sleep(.001)
#     for i in range(100, -23, -1):
#         print(i)
#         test.move_servo_position(0, i)
#         time.sleep(.001)

