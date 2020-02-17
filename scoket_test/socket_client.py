from socket import *

c_socket = socket(AF_INET,SOCK_STREAM)
host = ("127.0.0.1", 4526)
c_socket.connect(host)
while True:
    data  = input("客户端发送的消息是>>")
    if not data:
        break
    c_socket.send(bytes(data, "utf-8"))
    data = c_socket.recv(1024)
    print("客户端收到的消息是",data)
    print(str(data, "utf-8"))





