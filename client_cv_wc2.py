import cv2
import socket
import pickle
import struct

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(3, 320)
cap.set(4, 240)
# cap.set(cv2.CAP_PROP_FPS, 10)

print('Video Capture Online')
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.1.15', 9090))
print('Connection Online')

while True:
    ret, frame = cap.read()
    # Serialize frame
    data = pickle.dumps(frame)
    # print(data)
    # converts data length into bytes
    message_size = struct.pack("L", len(data))
    # checks message size
    msg_size = struct.unpack('L', message_size)[0]
    print(msg_size)
    # sends message size and data together
    clientsocket.sendall(message_size + data)
