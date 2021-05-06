import sys
import enum
import SensorLib

class Runtime(enum.Enum):
    Simulation = 0
    Test = 1
    REAL = 2

# state machine
class RState(enum.Enum):
    # Validate Launch Parameters and wait for Controller Input
        # Validate Power Source
        # Validate PHAT Servo
        # Validate Sensors
            # IMU 20949
            # XA110 GPS
            # CCS811
            # BME280
            # BMO080 (x2)
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


