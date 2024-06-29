import keyboard
import board
import time
import os
import board
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())


def main():
    while 1:

        if keyboard.is_pressed('up'):
            kit.stepper1.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )
            kit.stepper2.onestep(direction=stepper.FORWARD,style=stepper.SINGLE )

        if keyboard.is_pressed('down'):
            kit.stepper1.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )
            kit.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.SINGLE )

if __name__ == "__main__":
    main()
