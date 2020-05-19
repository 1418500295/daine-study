import os

from locust import *
import json
class UserBehavior(TaskSet):

    @task
    def getCookie(self):
        url = "http://localhost:8889/v1/getDemo"

        data = {
            "name": "daine",
            "age": "26"
        }
        response = self.client.get(url,params=data).json()
        print(response)

class user(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    # os.system("locust -f Locust_http.py --host=localhost --no-web -c 100 -r 20")
    os.system("locust -f Locust_http.py --host=localhost")