import sys
from enum import Enum
from enum_switch import Switch
from time import sleep
from flight import FlightClass
from control import ControlClass
from logger import Logger

f = FlightClass
c = ControlClass
l = Logger

if __name__ == '__main__':
    
    # Create File Lurk Before File
    l.LogLurk()
    
    # Flight Setup
    flight = f.flight
    
    # Set Flight Data
    f.SetFlightState(flight)
    f.flightSwitch(flight)
    
    # Control Setup
    control = c.control
    
    # Set Control Data
    c.SetControlState(control)
    c.controlSwitch(control)
    
    # Start Logging Data
    l.LogVisuals()
    l.LogInfo()