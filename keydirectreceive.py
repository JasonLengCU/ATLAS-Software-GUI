import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP
sock.connect((TCP_IP, TCP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode("utf-8")
    print(data)