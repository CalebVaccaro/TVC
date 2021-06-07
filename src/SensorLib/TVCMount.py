from pi_servo_hat import PiServoHat
import time

class Servos():
    
    def TestServos():
        
        # Initialize Constructor
        test = PiServoHat()
        
        test.set_pwm_frequency(100)
        
        # Restart Servo Hat (in case Hat is frozen/locked)
        test.restart()
        
        # Test Run
        #########################################
        # Moves servo position to 0 degrees (1ms), Channel 0
        test.move_servo_position(0, 45)

        # Moves servo position to 90 degrees (2ms), Channel 0
        test.move_servo_position(1, 45)
        
        # Moves servo position to 90 degrees (2ms), Channel 0
        test.move_servo_position(2, 45)
    loop = 3
    def TestServosContinuous():
        
        # Initialize Constructor
        test = PiServoHat()
        
        test.set_pwm_frequency(50)
        
        # Restart Servo Hat (in case Hat is frozen/locked)
        test.restart()
        
        # Test Run
        #########################################
        # Moves servo position to 0 degrees (1ms), Channel 0
        test.move_servo_position(0, 0)

        # Pause 1 sec
        time.sleep (1)
        
        
        # Sweep
        #########################################
        while Servos.loop > 0:
            for i in range(0, 90):
                print(i)
                test.move_servo_position(0, i)
                test.move_servo_position(2,i)
                time.sleep(.005)
            for i in range(45, 0, -1):
                print(i)
                test.move_servo_position(1, i)
                time.sleep(.005)
            Servos.loop = Servos.loop - 1


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

