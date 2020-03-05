from websocket import *


ws = create_connection("ws://127.0.0.1:1345/test/demo/?name=daine")


ws.send("hello daine")
print("接收中")
result = ws.recv()
print(result)
ws.close()


