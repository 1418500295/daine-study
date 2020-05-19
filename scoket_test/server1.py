from socket import *

s_scoket = socket(AF_INET,SOCK_STREAM)
address = ("127.0.0.1",4721)
s_scoket.bind(address)
s_scoket.listen(3)
while True:
    print("等待连接中。。")
    coon, addr = s_scoket.accept()
    print("连接来自",addr)
    while True:
        data = coon.recv(1024)
        print("服务端接收的数据是",data)
        if not data:
            break
        message = input("服务端发送的消息是")
        coon.send(bytes(message,'utf-8'))


