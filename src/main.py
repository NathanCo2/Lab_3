"""!
@file main.py

This program demonstrates our teams ability to utilize the three developed classes in lab to run a controller,
closed-loop step response test in which the set point is chanfed as to rotate the motor by about one revolution
and stop it at the final position. The code waits for the user to input a Kp value then runs the step response test
each time a value is entered. 

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-02-13 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""
# from matplotlib import pyplot
from motor_driver import MotorDriver
from encoder_reader import Encoder
from motor_controller_Nathan import MotorController
import utime


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


# Reads the com port and waits for Kp value

while True:
    usbvcp = pyb.USB_VCP()
    print('Receiving')
#     while True:
#         # Read data with a timeout of 100 milliseconds
#         KP_bytes = usbvcp.readline(100)
#         if KP_bytes:
#             break
        # Convert bytes to string, then float
    while True:
        KP = usbvcp.readline()
        if KP:
            break
    #print(KP)
    KP = float(KP.decode('utf-8'))
    #print(KP)
    #print(f"input recieved")
    #print(KP)

    # setup motor controller
    Jerry.zero()
    setpoint = 5000
    Deitch = MotorController(KP, setpoint, Tom.set_duty_cycle, Jerry.read)
        
    for i in range(200):
        Deitch.run()
        utime.sleep_ms(5)

    Deitch.controller_response()
    Tom.set_duty_cycle(0)
    KP = 0 # reset KP
    

