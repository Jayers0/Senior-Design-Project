import RPi.GPIO as GPIO
import gpiozero
import time


GPIO.setmode(GPIO.BCM)

warningLED =  gpiozero.LED(25)

def blinkLED(t = None):
    if t != None:
        for i in range(int(t)):
            warningLED.on()
            time.sleep(0.5)
            warningLED.off()
            time.sleep(0.5)
    else:
        for i in range(5):
            warningLED.on()
            time.sleep(0.5)
            warningLED.off()
            time.sleep(0.5)