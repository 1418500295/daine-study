
from socket import *

c_socket = socket(AF_INET,SOCK_STREAM)
host = ("127.0.0.1",4721)
c_socket.connect(host)
while True:
    message = input("客户端发送的消息是")
    if not message:
        break
    c_socket.send(bytes(message,'utf-8'))
    data = c_socket.recv(1024)
    print("客户端收到的消息是",data)
    print(str(data,'utf-8'))