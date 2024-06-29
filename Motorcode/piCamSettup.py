from multiprocessing.pool import ThreadPool
import threading
import os

def setupCamCommection():
    try:
        os.system('libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888')
    except:
        print("Unable to setup SPI connection to RPI cam.")

def setupYOLOv5():
    try:
        yolov5 = open('/home/sgstamp2/yolov5/detect.py','rt+')
        exec(str(yolov5.read()))
    except:
        print("Yolov5 model failed to initalize.")