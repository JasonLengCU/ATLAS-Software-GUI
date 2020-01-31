import pickle
import socket
import struct
import cv2
from datetime import datetime

HOST = ''
PORT = 8089

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

data = b'' ### CHANGED
payload_size = struct.calcsize("L")

while True:
    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    # print(msg_size)
    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    # print(len(data))
    # Extract frame
    frame = pickle.loads(frame_data)

    height, width, channels = frame.shape
    centx = round(width/2)
    centy = round(height/2)
    cv2.circle(frame, center=(centx, centy), radius=50, color=(0, 255, 0), thickness=5)
    cv2.rectangle(frame, pt1=(75, 75), pt2=(width-75, height-75), color=(0, 255, 0), thickness=5)
    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)