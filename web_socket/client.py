from websocket import *
ws = create_connection("ws://127.0.0.1:1348/test/demo/?name=daine")
ws.send("Hello, World")
print ("Reeiving...")
result = ws.recv()
print(result)
ws.close()


