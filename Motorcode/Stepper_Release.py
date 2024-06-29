import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

kit = MotorKit(address=0x60,i2c=board.I2C())
kit0 = MotorKit(address=0x61,i2c=board.I2C())


steppers = [kit.stepper1,kit.stepper2,kit0.stepper1,kit0.stepper2]

for s in steppers:
	try:
		s.release()
	except:
		print("No device named: ",s)