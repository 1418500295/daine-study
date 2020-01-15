
from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession
import os
import json


class UserBehavior(TaskSet):
    @task
    def job(self):
        url = "http://lhtttoutiao.sskk168.com"

        data = {
            "A": "get_home_head_detail_aes",
            "base": "aEdjNUtVeFM4ampwRG4zcVhmTy9QaUhuUnBjV1BIQUREYW9qVVUxUzFKaS9UWXdDcVhlRFRuT3dPeVVxZEJ6dGFHTXAwVTA0MGwvVGR0aVhDUURnT3lCeXhZbmNPZy8zNlVXWmF0Tnl3ZHVRRVpucVowTFpQdnJKS25LWEZteUlBdXMzYU5VQVFidmZ3TCt6Y2lHUDlmRHpxMzZPSl"
                    "g5QzJQMzBHQnpRZURma2VwYUlyREFMenVuOGRvVHpFdEVoeTVha3NwRUE1R1RpRkhxWkVVRTdQQT09&"
        }
        response = self.client.get(url, data=data).json()
        print(response)
        # assert response["status"] == 1




class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    os.system("locust -f operate_locust.py --host=lhtttoutiao.sskk168.com")