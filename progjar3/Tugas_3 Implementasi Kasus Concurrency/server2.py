import socket

SERVER_IP = '192.168.122.45'
SERVER_PORT = 5758

serverSock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP, UDP_PORT)))
filename='server2.jpg'
fp = open(filename,'wb+')
ditulis=0
count=0
while True:
    data, addr = serverSock.recvfrom(1024)
    count=count+len(data)
    print(addr, count, len(data), data)
    fp.write(data)