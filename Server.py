# server.py
#utf-8
import socket 

host = "91.151.93.119"
port = 1453

my_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
my_socket.bind((host , port))
my_socket.listen(2)
con , addr = my_socket.accept()

con.send(b"Server a hosgeldin | q ya bas ")
eski = "q"
while True:
    data = con.recv(1024)

    if data.decode() != eski:
        print(data.decode())
    if eski == data.decode():
        break
    #eski =data.decode()
    


my_socket.close()
