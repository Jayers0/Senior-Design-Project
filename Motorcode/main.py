#import readGPIO
#from readGPIO import *
from motorCommands import *
from ethernetComunication import *
from calibrateMaster import *
from lightTest import blinkLED


def KeyenceScan():
    i = input("Enter pass (p) or fail (f): ")
    if i == 'p':
        return True
    else: 
        return False

def main():
    masterMotorRelease()
    masterCalibrate()
    FlipAct0()
    print("")
    time.sleep(2)
    while 1: #this loop will be the main controll loop
        ExtendAct0()
        masterMotorRelease()
        
        time.sleep(5)
        RetractAct0()
        RetractAct1()
        scan = KeyenceScan()
        if scan:
            ExtendAct0(steps=1200)
            ExtendAct1(steps=800)
            time.sleep(.01)
            FlipAct0()
            RetractAct1()
            scan = KeyenceScan()
            if scan == True:
                ExtendAct1()
                time.sleep(3)
                FlipAct1()
                RetractAct1()
            else:
                ExtendAct1(800)
                RetractAct0()
                FlipAct1()
                blinkLED()
        else:
            ExtendAct0(1000)
            RetractAct1()
            FlipAct0()
            blinkLED()
            dstep_count = 0
            calibrateMotors()
        
    
main()