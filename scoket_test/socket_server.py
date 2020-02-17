from socket import *
from time import ctime

s_socket = socket(AF_INET, SOCK_STREAM)
host = ("127.0.0.1", 4526)
# 将主机与端口绑定到套接字
s_socket.bind(host)
# 设置并启动tcp监听器
s_socket.listen(5)
while True:
    print("等待连接中...")
    # 被动接受tcp连接
    coon, addr = s_socket.accept()
    print("连接到达",addr)
    while True:
        data = coon.recv(1024)
        print("服务端收到的消息是",data)
        if not data:
            break
        message = input("服务端发送的消息是>>")
        coon.send(bytes(message, "utf-8"))




