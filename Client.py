# client.py
import socket 

host = 172.31.45.208
port = 4646

my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
my_socket.connect((host, port))

data = my_socket.recv(1024)
print(data.decode())

while True:
    yazi = input("YAZ : ")
    my_socket.send(yazi.encode())


my_socket.close()


a = int(input("Ne söylemek istersiniz ? "))
