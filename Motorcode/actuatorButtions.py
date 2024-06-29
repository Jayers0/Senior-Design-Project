import RPi.GPIO as GPIO
import gpiozero
import time


GPIO.setmode(GPIO.BCM)

act1RearButtion= gpiozero.Button(23)
act0FrontButtion = gpiozero.Button(27)
act0RearButtion= gpiozero.Button(24)
act1FrontButtion = gpiozero.Button(22)
