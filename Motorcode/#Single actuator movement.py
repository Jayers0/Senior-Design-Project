#Single actuator movement

"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

from tqdm import tqdm, trange





choice = input("0 for address 0x60 \n 1 for address 0x61")
choice = str(choice)
if choice == 0:
    Actuator1 = MotorKit(address=0x60, i2c=board.I2C())
elif choice == 1:
    Actuator1 = MotorKit(address=0x61, i2c=board.I2C())
else:
    print("SELECT A MOTOR DUMMY")


def masterMotorRelease(id=None):  
    if id== None:
        Actuator1.stepper1.release()
        time.sleep(.1)
        Actuator1.stepper2.release()
        time.sleep(.1)


for i in range(1050):
    Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
for i in range(1050):
    Actuator1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
for i in range(1050):
    Actuator1.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
for i in range(1050):
    Actuator1.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )

masterMotorRelease()

for i in range(50):
    Actuator1.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE )
    time.sleep(0.01)
for i in range(50):
    Actuator1.stepper2.onestep(direction=stepper.FORWARD,style=stepper.DOUBLE )
    time.sleep(0.01)
masterMotorRelease()