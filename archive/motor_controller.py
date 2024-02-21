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
from matplotlib import pyplot

class MotorController():
    """! 
    This class implements the Motor Controller for an ME405 kit. 
    """

    def __init__ (self, gain, setpoint, setdutycycle_f, getactual_f):
        """! 
        Creates an motor controller object that can be used to set 
        the gain and setpoint of the motor
        """
        self.setpoint = setpoint
        self.gain = gain
        self.actual = 0
        self.err = 0
        self.setdutycycle = setdutycycle_f
        self.getactual = getactual_f
        
    def run(self):
        """!
        This method will repeatedly run the controll algorithm
        """
        #Calculating the error signal (actuation signal)
        self.actual = self.getactual()
        self.err = self.setpoint - self.actual
        self.PWM = int(self.err*self.gain)
        self.setdutycycle(self.PWM)
        return self.PWM # return actuation value
        
    def set_setpoint(self, setpoint):
        """!
        This method sets up the setpoint for proportional control
        """
        self.setpoint = setpoint
        
    def set_Kp(self, gain):
        """!
        This method sets up the gain for proportional control
        """
        self.gain = gain
        
    def controller_response(self):
        """!
        This method will print the results obtained of the step
        response and print when the step response is done running
        """
        with serial.Serial(port='COM5',baudrate=9600,timeout=1) as ser:
            ser.write(b'\x03') 
            ser.write(b'\x04')
            
            for line in ser:
                try:
                    line = line.decode('utf-8')
                    #splits the string into two CSV
                    split = line.split(',')
                    #creates a list of the x-values (Time [s])
                    x = split[0:1]
                    join_x = ','.join(x)
                    xx = float(join_x)
                    #creates a list of the y-values (Voltage [V])
                    y = split[1:2]
                    join_y = ','.join(y)
                    yy = float(join_y)
                    #stores the created list of variables in new arrays
                    xaxis_times.append(xx)
                    yaxis_voltage.append(yy)
                except ValueError:
                    print('Error: :(')
                    pass

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


