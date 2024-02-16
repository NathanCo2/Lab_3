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
#     usbvcp = pyb.USB_VCP()
    print('Input:')
#     while True:
#         # Read data with a timeout of 100 milliseconds
#         KP_bytes = usbvcp.readline(100)
#         if KP_bytes:
#             break
    KP_bytes = input()
    KP = float(KP_bytes)
    #KP = float(KP_bytes.decode('utf-8'))
    #print(f"input recieved")
    #print(KP)

    # setup motor controller
    Jerry.zero()
    setpoint = 30500
    Deitch = MotorController(KP, setpoint, Tom.set_duty_cycle, Jerry.read)
        
    for i in range(200):
        Deitch.run()
        utime.sleep_ms(10)

    Deitch.controller_response()
    Tom.set_duty_cycle(0)
    

