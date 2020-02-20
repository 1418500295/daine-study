from websocket import *


ws = create_connection("ws://127.0.0.1:1244/test/demo/1")

ws.send("Hello, World")

print("接受中")
result = ws.recv()
print(result)
ws.close()
