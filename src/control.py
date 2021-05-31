from enum import Enum
from enum_switch import Switch
from time import sleep
import Validation
import data

# state machine
class RState(Enum):
    # Validate Launch Parameters and wait for Controller Input
        # Validate Power Source
        # Validate PHAT Servo
        # Validate Sensors
            # IMU 20948
            # GPS XA110 
            # CCS811
            # BME280
            # IMU BMO080 (x2)
        # Validate Servo Motor
            # X and Y Servo Motors (0 , 1 Channels)
    # Validate TVC Code
    # Pass Validation
    ValidateLaunch = 0
    # Ignition is Set waiting for Launch
    ARMED = 1
    # Ignition of Motor, start of Liftoff, unexpected Torque on Body
    Ignition = 9
    # Lifting off Launch Pad and Highest Control PID due to most Thrust/Torque on Body
    Liftoff = 2
    # Motor has burned out, awaiting Apogee, closest point to apogee
    BurnOut = 3
    # Body has traveled to the highest altitude, starting to fall back down
    Apogee = 4
    # Body is in free fall under aerodynamic forces
    FreeFall = 5
    # Ejection charged is fired, deploying Parachute
    Ejection = 6
    # Body has landed on the ground
    Touchdown = 7
    # Completed Flight
    Completed = 8

class ControlSwitch(Switch):
    def ValidateLaunch(self):
        ControlClass.ValidateLaunch()
        return "Validated Launch"

    def ARMED(self):
        return "ARMED"

    def Ignition(self):
        return "Ignition"
    
    def Liftoff(self):
        return "Liftoff"
    
    def BurnOut(self):
        return "BurnOut"
    
    def Apogee(self):
        return "Apogee"
    
    def FreeFall(self):
        return "FreeFall"
    
    def Ejection(self):
        return "Ejection"
    
    def Touchdown(self):
        return "Touchdown"
    
    def Completed(self):
        return "Completed"

class ControlClass():

    control = RState.ValidateLaunch
    controlSwitch = ControlSwitch(RState)
    
    def GetControlState():
        return control
        
    def SetControlState(state):
        control = state
        
    # CONTROL STATES

    def ValidateLaunch():
        print("Validating Launch Components...")
        sleep(.5)
        Validation.ValidateBattery()
        sleep(1)
        Validation.ValidateSensors()
        
    def ARMED():
        sleep(2)
        print("ARMING ROCKET...HEADS UP")
        
    