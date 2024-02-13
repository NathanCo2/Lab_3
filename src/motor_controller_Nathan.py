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

class MotorController:
    """! 
    This class implements the Motor Controller for an ME405 kit. 
    """

    def __init__ (self, gain, setpoint, setdutycycle_f, getactual_f):
        """! 
        Creates an encoder object that can be used to measure
        the position of a motor
        @param gain = Kp, percent duty cycle/encoder count
        @param setpoint = desired angle of motor
        """
        self.setpoint = setpoint
        self.gain = gain
        self.actual = 0
        self.err = 0
        self.setdutycycle = setdutycycle_f
        self.getactual = getactual_f
        
    def run(self):
        """!
        This method will run one pass of the control algorithm
        """
        # error calcs (PWN = e_setpoint - e_actual)
        self.actual = self.getactual()
        self.err = self.setpoint - self.actual
        self.PWM = self.err*self.gain
        self.setdutycycle(self.PWM)
        
    
    def set_setpoint(self,setpoint):
        """!
        This method sets up the setpoint for proportional control
        """
        self.setpoint = setpoint
        
    def set_Kp(self,gain):
        """!
        This method sets up the gain for proportional control
        """
        self.gain = gain
        
    def controller_response(self):
        """!
        This method will print the results obtained of the step
        response and print when the step response is done running
        """  

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":
    # set up timer 8 for encoder 2
    TIM8 = pyb.Timer(8, prescaler=1, period=0xFFFF) # Timer 8, no prescalar, frequency 100kHz
    #Define pin assignments for encoder 2
    pinc6 = pyb.Pin(pyb.Pin.board.PC6)
    pinc7 = pyb.Pin(pyb.Pin.board.PC7)
    # Create encoder object
    Jerry = Encoder(pinc6, pinc7, TIM8)

    # setup motor
    TIM5 = pyb.Timer(5, freq=2000) # Timer 5, frequency 2000Hz
    # Define pin assignments for motor 2
    pinc1 = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
    pina0= pyb.Pin(pyb.Pin.board.PA0)
    pina1 = pyb.Pin(pyb.Pin.board.PA1)    
    # Create motor driver
    Tom = MotorDriver(pinc1, pina0, pina1, TIM5)

    # setup motor controller
    kP = 1
    setpoint = 1
    Deitch = MotorController(kP, setpoint, Tom.set_duty_cycle, Jerry.read)
        




