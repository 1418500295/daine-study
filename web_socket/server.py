from pywss import *

@route("/test/demo/1")
def demo(request, data):
    return data

if __name__ == '__main__':
    ws = Pyws(__name__,address="127.0.0.1",port=1344)
    ws.serve_forever()