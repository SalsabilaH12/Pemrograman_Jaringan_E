import socket

# Alpine 2 : 192.168.122.154
# Alpine 3 : 192.168.122.244
# Alpine 4 : 192.168.122.177
# Alpine 5 : 192.168.122.121

#ip diubah sesuai ip masing masing alpine
SERVER_IP = '192.168.122.154'
SERVER_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", SERVER_PORT))



while True:
    data, addr = sock.recvfrom(1024)
    #buffer size 1024
    print(addr)
    print("diterima ", data)
    print("dikirim oleh " , addr)