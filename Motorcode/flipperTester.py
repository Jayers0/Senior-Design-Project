"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

Actuators = MotorKit(address=0x62 ,i2c=board.I2C())
Flippers = MotorKit(address=0x62,i2c=board.I2C())
dstep_count = 0
#mode = input("please enter the mode you want to test the motors:")

def masterMotorRelease(id=None):
    if id== None:
        Actuators.stepper1.release()
        Actuators.stepper2.release()
        Flippers.stepper1.release()
        Flippers.stepper2.release()
    elif id==1:
        Actuators.stepper1.release()
    elif id==2:
        Actuators.stepper2.release()
    elif id==3:
        Flippers.stepper1.release()
    elif id==4:
        Flippers.stepper2.release()
    else:
        print("Invalid motor selection")

act = Actuators.stepper1

for Style in [stepper.DOUBLE,stepper.SINGLE,stepper.DOUBLE]:
    masterMotorRelease()
    for i in range(100):
        print("testing style: ",Style,"with timeing: ",i/100,"seconds")
        for i in range(50):
            act.onestep(direction=stepper.BACKWARD,style=Style)
            time.sleep(i/100)
    
        for i in range(50):
        #while !plate_limit_switch
            act.onestep(direction=stepper.FORWARD,style=Style)
            time.sleep(i/100)