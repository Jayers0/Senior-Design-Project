import RPi.GPIO as GPIO
import gpiozero
import time

triggerPin =40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin,GPIO.OUT)

while 1:
    print(0)
    GPIO.output(triggerPin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(triggerPin,GPIO.LOW)


