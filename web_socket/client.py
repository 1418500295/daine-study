# import websocket
# url = 'ws://47.57.7.137:9512'  #websocket连接地址
# ws = websocket.create_connection(url)  #创建连接
# '''data为json格式'''
# ws.send("哈哈哈")   #json转化为字符串，必须转化
# print(ws.recv())    #服务器响应数据
# ws.close()   #关闭连接
from websocket import create_connection

ws = create_connection(url="ws://127.0.0.1:1348/test/demo?name=daine")
ws.send("hello")
print(ws.recv())