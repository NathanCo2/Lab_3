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
        self.setpoint = 0
        self.actual = 0
        self.gain = 0
        self.PWM = 0
    
    def run(self):
        """!
        This method will repeatedly run the controll algorithm
        """
        # error calcs (PWN = e_setpoint - e_actual)
        self.PWM = gain(self.setpoint - self.actual)
    
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
        #Creates empty array
        xaxis_times = []
        yaxis_height = []

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
                return (xaxis_times, yaxis_height)
         
if __name__ == "__main__":




