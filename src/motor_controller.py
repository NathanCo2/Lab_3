"""!
@file encoder_reader.py

This program demonstrates the development of a class called Encoder to measure
the movement of a motor using an optical encoder. This code was tested an ran
with the Motor Driver class developed in Lab 1 to examine if the code was running
correctly. 

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-02-06 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""

import pyb
import time
from motor_driver import MotorDriver
from encoder_reader import Encoder

class Encoder:
    """! 
    This class implements a Encoder for an ME405 kit. 
    """

    def __init__ (self, ch1pin, ch2pin, timer):
        """! 
        Creates an encoder object that can be used to measure
        the position of a motor
        @param ch1pin: Pin for reading encoder channel 1
        @param ch2pin: Pin for reading encoder channel 2
        @param timer: Timer object for reading encoder
        """
        
    def read(self):
        """!
        This method returns the current position of the
        motor using the encoder
        """

        
    def zero(self):
        """!
        This method sets the encoder count to zero at the
        current position of the motor
        """
        

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":




