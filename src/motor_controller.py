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

    def __init__ (self, gain, setpoint, PWM_function, position_function):
        """! 
        Creates an motor controller object that can be used to set 
        the gain and setpoint of the motor
        """
        #print ("Creating an setpoint and gain")
        self.gain = gain
        self.setpoint = setpoint
        self.actual = actual
        self.error = error
        
    def run(self):
        """!
        This method will repeatedly run the controll algorithm
        """
        #Calculating the error signal (actuation signal)
        self.error = self.gain(self.setpoint - self.position_function())
        
        
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
        #opens the data file from folder and reads
        with open('data.csv', 'r') as file: 
            #store column headers for first row by characters  
            header = file.readline(-1)
            time = header[:8]
            height = header[10:20]
            #iterates through each line of data file 
            for line in file:
                try:
                    #splits each line where comma is present
                    split = line.split(',')
                    #Creates a list of the X-values (Time [s])
                    x = split[0:1]#grabs first column
                    join_x = ','.join(x)#combines 2 strings together
                    xx = float(join_x)
                    #Creates a list of the Y-values (Height [m])
                    y = split[1:2]
                    join_y = ','.join(y) 
                    yy = float(join_y)
                    #stores the created list of variables in the blank arrays
                    xaxis_times.append(xx)
                    yaxis_height.append(yy)
                    #Creates points for plot
                    #print(xaxis_times, yaxis_height)   
                except ValueError:
                    #error occurs when float runs
                    print('Error: Not a integer')
                    pass

# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program           
if __name__ == "__main__":




