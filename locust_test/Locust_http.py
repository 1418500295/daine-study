import os

from locust import *
import json
class UserBehavior(TaskSet):

    @task
    def getCookie(self):
        url = "http://localhost:8889/postDemo"
        headers = {
            "content-type": "application/json"
        }
        data = {
            "name": "james",
            "age": "23"
        }
        response = self.client.post(url=url,data=json.dumps(data),headers=headers)
        print(response.text)

class user(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    os.system("locust -f Locust_http --host=localhost")