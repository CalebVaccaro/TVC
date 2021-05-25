import sys
from enum import Enum
from enum_switch import Switch
from time import sleep
from flight import FlightClass
from control import ControlClass


f = FlightClass
c = ControlClass

if __name__ == '__main__':
    
    # Flight Setup
    flight = f.flight
    print(flight)
    
    # Set Flight Data
    f.SetFlightState(flight)
    print(f.flightSwitch(flight))
    
    # Control Setup
    control = c.control
    
    # Set Control Data
    c.SetControlState(control)
    print(c.controlSwitch(control))
    
    