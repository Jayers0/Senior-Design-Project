import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from readGPIO import *
from tqdm import tqdm, trange
from calibrateMaster import *
from ComponentCalibrations.calibrateACT0 import *
from ComponentCalibrations.calibrateACT1 import *
from actuatorButtions import *

Actuator0_StepLength = 0
Actuator1_StepLength = 0

def ExtendAct1(calibrateMode = None,steps = None):
    if steps == None:
        if calibrateMode == True:
            global Actuator1_StepLength
            while act1FrontButtion.is_pressed == False:
                Actuator0.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
                Actuator1_StepLength = Actuator1_StepLength + 1
                print(Actuator1_StepLength)
        else:
            while not act1FrontButtion.is_pressed:
                Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
    else:
        for i in range(steps):
            Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
    masterMotorRelease()

def RetractAct1():
    while act1RearButtion.is_pressed == False:
        Actuator1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
    masterMotorRelease()

def ExtendAct0(calibrateMode = None, steps = None):
    if calibrateMode == True:
        global Actuator0_StepLength
        while act0RearButtion.is_pressed == False:
            Actuator0.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
            Actuator0_StepLength = Actuator0_StepLength + 1
            print(Actuator0_StepLength)
    elif steps is not None:
        for i in range(steps):
            Actuator0.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )    
    else:
        while act0FrontButtion.is_pressed == False:
            Actuator0.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
        masterMotorRelease()

def RetractAct0():
    while act0RearButtion.is_pressed == False:
        Actuator0.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
    masterMotorRelease()

def FlipAct0():
    masterMotorRelease()
    for i in range(90):
        Actuator0.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        time.sleep(0.015)
    masterMotorRelease()
    for i in range(30):
        Actuator0.stepper2.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
        time.sleep(0.015)
    masterMotorRelease()
def FlipAct1():
    masterMotorRelease()
    for i in range(70):
        Actuator1.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
        time.sleep(0.02)
    masterMotorRelease()
    for i in range(30):
        Actuator1.stepper2.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
        time.sleep(0.02)
    masterMotorRelease()