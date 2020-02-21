import os
import time

import websocket
from locust import events, Locust, TaskSet, task


class WebSocketClient(object):

    def __init__(self, host):
        self.host = host
        self.ws = websocket.WebSocket()

    def connect(self, burl):
        start_time = time.time()
        try:
            self.conn = self.ws.connect(url=burl)
        except websocket.WebSocketTimeoutException as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="websockt", name='urlweb', response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="websockt", name='urlweb', response_time=total_time, response_length=0)
        return self.conn

    def recv(self):
        return self.ws.recv()

    def send(self, msg):
        self.ws.send(msg)

class WebsocketLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(WebsocketLocust, self).__init__(*args, **kwargs)
        self.client = WebSocketClient(self.host)


class SupperDianCan(TaskSet):

    @task
    def test_baidu(self):
        self.url = 'wss://echo.websocket.org'
        self.data = {}

        self.client.connect(self.url)
        while True:
            recv = self.client.recv()
            print(recv)
            if eval(recv)['type'] == 'keepalive':
                self.client.send(recv)
            else:
                self.client.send(self.data)


class WebsiteUser(WebsocketLocust):

    task_set = SupperDianCan

    min_wait=1000

    max_wait=3000

if __name__ == '__main__':
    os.system("locust -f Locust_websocket.py --host=echo.websocket.org")