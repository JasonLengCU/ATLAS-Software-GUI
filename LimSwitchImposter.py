import socket

host = "localhost"
port = 5556
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# try:
#     s.bind((host, port))
#     print('Outgoing Port Bound')
# except socket.error as e:
#     print(str(e))

cmdout = '111'
while 1:
    s.sendto(cmdout.encode('utf-8'), ("127.0.0.1", 5556))