from enum import Enum
from enum_switch import Switch

class FlightSwitch(Switch):
    def Sim(self):
        return "Sim"

    def Test(self):
        return "Test"

    def REAL(self):
        return "REAL"
        
class Flight(Enum):
    Sim = 0
    Test = 1
    REAL = 2
        

class FlightClass():
    
    flightSwitch = FlightSwitch(Flight)
    flight = Flight.Sim

    def GetFlightState():
        return flight
        
    def SetFlightState(state):
        flight = state

    # SIMULATION STATES

    def Sim():
        print("Simulaton Flight")

    def Test():
        print ("Test Flight")
        
    def REAL():
        print("REAL FLIGHT!!!")

