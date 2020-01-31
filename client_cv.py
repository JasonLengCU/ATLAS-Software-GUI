import cv2
import socket
import pickle
import struct

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

print('Video Capture Online')
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.43.136', 8089))
print('Connection Online')

while True:
    ret, frame = cap.read()
    # Serialize frame
    data = pickle.dumps(frame)
    # print(data)
    # converts data length into bytes
    message_size = struct.pack("L", len(data))
    print(len(data))
    # checks message size
    msg_size = struct.unpack('L', message_size)[0]
    print(msg_size)
    # sends message size and data together
    clientsocket.sendall(message_size + data)
