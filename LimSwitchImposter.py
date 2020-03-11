import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # UDP
s.connect((TCP_IP, TCP_PORT))

# cmdout = '1111'
n = 0
while 1:
    if n == 0:
        cmdout = '1111'
        n += 1
    elif n == 1:
        cmdout = '0111'
        n+=1
    elif n == 2:
        cmdout = '0000'
        n = 0
    print(cmdout)
    s.sendto(cmdout.encode('utf-8'), ("127.0.0.1", 5556))