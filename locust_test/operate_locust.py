
from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession
import os
import json


class UserBehavior(TaskSet):
    # @task
    # def job(self):
    #     url = "http://lhtttoutiao.sskk168.com"
    #
    #     data = {
    #         "A": "get_home_head_detail_aes",
    #         "base": "aEdjNUtVeFM4ampwRG4zcVhmTy9QaUhuUnBjV1BIQUREYW9qVVUxUzFKaS9UWXdDcVhlRFRuT3dPeVVxZEJ6dGFHTXAwVTA0MGwvVGR0aVhDUURnT3lCeXhZbmNPZy8zNlVXWmF0Tnl3ZHVRRVpucVowTFpQdnJKS25LWEZteUlBdXMzYU5VQVFidmZ3TCt6Y2lHUDlmRHpxMzZPSl"
    #                 "g5QzJQMzBHQnpRZURma2VwYUlyREFMenVuOGRvVHpFdEVoeTVha3NwRUE1R1RpRkhxWkVVRTdQQT09&"
    #     }
    #     response = self.client.get(url, data=data).json()
    #     print(response)
        # assert response["status"] == 1



    # 获取令牌接口
    @task
    def get_token(self):
        url = "http://202.153.5.186:18080/admin/user/get_token"
        header = {
            "nonce": "123456",
            "sign": "bf63c88b469bf74b8f971a47d991b657999d5169",
            "timestamp": "1579136885",
        }
        data = {
            "userId": "5W5p5pRR",
            "clientId": "D81FFE35-184F-465b-9AD1-B3C01504902B"
        }

        response = self.client.post(url, data=json.dumps(data), headers=header)
        print(response.json())

    # @task
    # def get_info(self):
    #     url = "http://202.153.5.186:18080/admin/user/get_token"
    #     header = {
    #         "nonce": "123456",
    #         "sign": "bf63c88b469bf74b8f971a47d991b657999d5169",
    #         "timestamp": "1579136885",
    #     }
    #     data = {
    #         "userId": "5W5p5pRR"
    #     }
    #     response = self.client.post(url, data=json.dumps(data), headers=header)
    #     print(response.json())


class User(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000

if __name__ == '__main__':
    # os.system("locust -f operate_locust.py --host=lhtttoutiao.sskk168.com")
    os.system("locust -f operate_locust.py --host=202.153.5.186")