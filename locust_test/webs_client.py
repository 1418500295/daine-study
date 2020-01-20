import gzip
import json
import os
import time

import websocket
from locust import TaskSet, events, Locust, task


class WebSocketClient(object):

    def connect(self, url):
        # try:
        self.ws = websocket.WebSocketApp(url)
        self.ws.on_message = self.on_message
        self.ws.on_error = self.on_error
        self.ws.on_close = self.on_close
        # except websocket.WebSocketTimeoutException as e:
        #     events.request_failure.fire(request_type="web_socket", name='ws', response_time=time.time(), exception=e)
        # else:
        #     events.request_success.fire(request_type="web_socket", name='ws', response_time=time.time(),
        #                                 response_length=0)
        return self.ws

    def on_message(self, message):
        if isinstance(message, bytes):
            message = gzip.decompress(message).decode("utf-8")
        message = json.loads(message)
        print(message)
        if isinstance(message, dict):
            if 'ping' in message:
                pong = {'pong': message['ping']}
                self.ws.send(json.dumps(pong))

    def on_error(self, error):
        print('!!! error !!!', error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        print('opened')
        data = {"sub": {'category': 0, 'star': []}}
        self.ws.send(json.dumps(data))


class WebSocketLocust(Locust):
    def __init__(self):
        super(WebSocketLocust, self).__init__()
        self.client = WebSocketClient()


class UserBehavior(TaskSet):
    def on_start(self):
        print('--------- task start ------------')
        # self.url = "ws://202.153.5.186:9200?type=app"
        self.url = "ws://echo.websocket.org:80"

    def on_stop(self):
        print('---------- task stop ------------')

    @task
    def test_ws(self):
        ws = self.client.connect(self.url)
        ws.run_forever()


class WebsiteUser(WebSocketLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

if __name__ == '__main__':
    os.system("locust -f webs_client.py --host=202.153.5.186")