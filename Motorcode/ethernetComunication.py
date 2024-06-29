import socket

BufferSize = 1024
Port = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cammera_ip = '192.168.0.10'


def checkCamConnection(cammera_ip):
    global s
    try:
        s.connect(cammera_ip)
        return True
    except:
        return False


def signalScanReady():
    s.send("ready")
