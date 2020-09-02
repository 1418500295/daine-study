import os

from locust import *
from locust.contrib.fasthttp import FastHttpLocust
import json
class UserBehavior(TaskSet):

    @task
    def demo(self):
        url = "https://vapi.sskk168.com/v1/download?merchant_id=11"

        response = self.client.get(url).json()
        print(response)

class user(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 20000
if __name__ == '__main__':
    # os.system("locust -f Locust_http.py --host=localhost --no-web -c 100 -r 20")
    os.system("locust -f Locust_http.py --host=vapi.sskk168.com")