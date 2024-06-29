from ComponentCalibrations.calibrateACT0 import calibrateACT0 ,act1FrontButtion,act1RearButtion
from ComponentCalibrations.calibrateACT1 import calibrateACT1, act0FrontButtion, act0RearButtion
#from motorCommands import FlipAct0, FlipAct1
from lightTest import blinkLED
from connectionDiag import checkI2C
from piCamSettup import *
import os
import threading
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import board
import time

Actuator1 = MotorKit(address=0x61, i2c=board.I2C())
Actuator0 = MotorKit(address=0x60,i2c=board.I2C())

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

def masterCalibrate():
    #check all communication
    #Motor controll boards are conneced at I2C adress 0x60 and 0x61
    checkI2C(devices=['0x60', '0x61'])

    print("----------------------------------------\n Setting up SPI Cammera\n----------------------------------------")
    #setupCamCommection() # function is not currently functional
    print("----------------------------------------\n Initialzing YOLOv5 Inference \n----------------------------------------")
    #setupYOLOv5() #Function works but needs the previous fuction to work
    
    #Release all connected motors
    masterMotorRelease()

    #Calibrate linear actuator 0
    calibrateACT0()
    #FlipAct0()
    print("----------------------------------------\nLinear Actuator 0 connected and possitioned for start")
    #Calibrate linear actuator 1
    calibrateACT1()
    print("Linear Actuator 1 connected and possitioned for start")
    
    

    print("testing warning LED")
    blinkLED()

def calibrateMotors():
    #Release all connected motors
    masterMotorRelease()
    if act0FrontButtion.is_pressed == True:
        for i in range(100):
            Actuator0.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE)
    elif act0RearButtion.is_pressed == True:
        for i in range(100):
            Actuator0.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE)
    if act1FrontButtion.is_pressed == True:
        for i in range(100):
            Actuator1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE)
    elif act1RearButtion.is_pressed == True:
        for i in range(100):
            Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE)
    #Calibrate linear actuator 0
    calibrateACT0()
    print("----------------------------------------\nLinear Actuator 0 connected and possitioned for start")
    #Calibrate linear actuator 1
    calibrateACT1()
    print("Linear Actuator 1 connected and possitioned for start")

