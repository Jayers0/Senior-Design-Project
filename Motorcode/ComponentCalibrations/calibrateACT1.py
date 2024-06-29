import time
import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import atexit

from actuatorButtions import *

def exit_handler():
    masterMotorRelease();

atexit.register(exit_handler)
from tqdm import tqdm, trange

Actuator1 = MotorKit(address=0x61, i2c=board.I2C())
Actuator0 = MotorKit(address=0x60,i2c=board.I2C())
dstep_count = 0

def masterMotorRelease(id=None):
    
    if id== None:
        Actuator1.stepper1.release()
        time.sleep(.1)
        Actuator1.stepper2.release()
        time.sleep(.1)
        Actuator0.stepper1.release()
        time.sleep(.1)
        Actuator0.stepper2.release()
        time.sleep(.1)
    elif id==1:
        Actuator1.stepper1.release()
    elif id==2:
        Actuator1.stepper2.release()
    elif id==3:
        Actuator0.stepper1.release()
    elif id==4:
        Actuator0.stepper2.release()
    else:
        print("Invalid motor selection")

def calibrateACT1():
    global dstep_count
    while not act1FrontButtion.is_pressed:
        Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
    masterMotorRelease()
    while not act1RearButtion.is_pressed:
        Actuator1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        dstep_count+=1
    for i in range(int(dstep_count/2)-500):
        Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
    return 0

