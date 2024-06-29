"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import atexit

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

def stepThrough():
    c = None
    while(c == None):
        c = input("press any letter key to continue:")

actuators = {Actuator0,Actuator1}
while 1:
    stepThrough()
    for kit in actuators:
        masterMotorRelease()
        for i in range(1050):
            kit.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
        for i in range(1050):
            kit.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        for i in range(1050):
            kit.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        stepThrough()
        for i in range(1050):
            kit.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )

        masterMotorRelease()
        stepThrough()
        for k in actuators:
            if k == kit:
                pass
            else:
                for i in range(600):
                    k.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        stepThrough()
        for i in trange(55):
            kit.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE )
            time.sleep(0.0175)
        masterMotorRelease()
        for i in trange(55):
            kit.stepper2.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE )
            time.sleep(0.0175)
        masterMotorRelease()
        stepThrough()
        for k in actuators:
            if k == kit:
                pass
            else:
                for i in range(600):
                    k.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
        
    masterMotorRelease()



     #https://www.thingiverse.com/thing:1105305/files
    #https://realpython.com/python-command-line-arguments/
