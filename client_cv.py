import cv2
import socket
import pickle
import struct

cap = cv2.VideoCapture(0)

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))

while True:
    ret, frame = cap.read()
    # Serialize frame
    data = pickle.dumps(frame)
    # converts data length into bytes
    message_size = struct.pack("L", len(data))
    # checks message size
    msg_size = struct.unpack('L', message_size)[0]
    print(msg_size)
    # sends message size and data together
    clientsocket.sendall(message_size + data)
