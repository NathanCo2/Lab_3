"""!
@file main.py
Run real or simulated dynamic response tests and plot the results. This program
demonstrates a way to make a simple GUI with a plot in it. It uses Tkinter, an
old-fashioned and ugly but useful GUI library which is included in Python by
default.

This file is based loosely on an example found at
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Jessica Perez, Jacquelyn Banh, and Nathan Chapman
@date   2024-02-14 Original program, based on example from above listed source
@copyright (c) 2024 by Jessica Perez, Jacquelyn Banh, and Nathan Chapman and released under the GNU Public Licenes V3
"""
import utime
from motor_driver import MotorDriver
from encoder_reader import Encoder
from motor_controller_Nathan import MotorController
# from matplotlib import pyplot

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
kP = 0.0195
setpoint = 10000
Deitch = MotorController(kP, setpoint, Tom.set_duty_cycle, Jerry.read)
    
while True:
    Deitch.run()
    utime.sleep_ms(100)

