import cv2
import socket
import pickle
import struct
import time

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(3, 320)
cap.set(4, 240)
# cap.set(cv2.CAP_PROP_FPS, 2)

print('Video Capture Online')
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsocket.connect(('192.168.43.136', 8090))
print('Connection Online')


fpsLimit = 1/30 # throttle limit
startTime = time.time()
while True:
    ret, frame = cap.read()
    frame = rescale_frame(frame, percent=40)
    nowTime = time.time()
    if (nowTime - startTime) > fpsLimit:
        # Serialize frame
        data = pickle.dumps(frame)
        # print(data)
        # converts data length into bytes
        message_size = struct.pack("L", len(data))
        # checks message size
        msg_size = struct.unpack('L', message_size)[0]
        print('Message Size:')
        print(msg_size)
        # sends message size and data together
        clientsocket.sendall(message_size + data)
        startTime = time.time()
