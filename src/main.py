# from matplotlib import pyplot
from motor_driver import MotorDriver
from encoder_reader import Encoder
from motor_controller import MotorController
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

# setup motor controller
kP = 1
setpoint = 1
Deitch = MotorController(kP, setpoint, Tom.set_duty_cycle, Jerry.read)
    
    
while True:
    moe.set_duty_cycle (-50)#Reverse at 50% duty cycle
    #read encoder 20times for 20 seconds
    utime.sleep_ms(10)
    Tom.read()






# #Creates empty array
# xaxis_times = []
# yaxis_height = []

# #opens the data file from folder and reads
# with open('data.csv', 'r') as file: 
#     #store column headers for first row by characters  
#     header = file.readline(-1)
#     time = header[:8]
#     height = header[10:20]
#     #iterates through each line of data file 
#     for line in file:
#         try:
#             #splits each line where comma is present
#             split = line.split(',')
#             #Creates a list of the X-values (Time [s])
#             x = split[0:1]#grabs first column
#             join_x = ','.join(x)#combines 2 strings together
#             xx = float(join_x)
#             #Creates a list of the Y-values (Height [m])
#             y = split[1:2]
#             join_y = ','.join(y) 
#             yy = float(join_y)
#             #stores the created list of variables in the blank arrays
#             xaxis_times.append(xx)
#             yaxis_height.append(yy)
#             #Creates points for plot
#             #print(xaxis_times, yaxis_height)   
#         except ValueError:
#             #error occurs when float runs
#             print('Error: Not a integer')
#             pass
#     #plots the values (x,y) values stored in array
#     pyplot.plot(xaxis_times, yaxis_height)
#     pyplot.xlabel('Time [s]')
#     pyplot.ylabel('Height [m]')
#     pyplot.grid(True)
#     pyplot.show()
