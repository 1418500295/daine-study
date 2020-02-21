from websocket import *


ws = create_connection("ws://127.0.0.1:1244/test/demo/1")

ws.send("hello daine")
print("接收中")
result = ws.recv()
print(result)


