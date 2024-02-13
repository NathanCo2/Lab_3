"""!
@file motor_controller.py

This program demonstrates the development of a class called MotorController to that
perform closed-loop proportional control. This code was tested an ranwith the Motor
Driver class and Encoder clas developed in Lab 1 to examine if the code was running
correctly. 

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-02-13 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""

import pyb
import time
from motor_driver import MotorDriver
from encoder_reader import Encoder

class MotorController:
    """! 
    This class implements the Motor Controller for an ME405 kit. 
    """

    def __init__ (self, gain, setpoint, ch1pin, ch2pin, timer):
        """! 
        Creates an encoder object that can be used to measure
        the position of a motor
        @param ch1pin: Pin for reading encoder channel 1
        @param ch2pin: Pin for reading encoder channel 2
        @param timer: Timer object for reading encoder
        """
    
    def run(self):
        """!
        This method will repeatedly run the controll algorithm
        """
    
    
    def set_setpoint(self):
        """!
        This method sets up the setpoint for proportional control
        """

        
    def set_Kp(self):
        """!
        This method sets up the gain for proportional control
        """
    
    def controller_response(self):
        """!
        This method will print the results obtained of the step
        response and print when the step response is done running
        """  

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":




