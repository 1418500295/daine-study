import gevent
from gevent import monkey

monkey.patch_all()

from multiprocessing import Process
import requests, time, httpx
import datetime
from others.test_kk_interfaces import KKInterface


class ApiTest():

    def __init__(self):

        self.gevent_num = 100  # 开启的协程数
        self.task_num = 2  # 开启的进程数
        self.req_url = "http:"
        self.req_data = {
            "coinid": ""
      
        }
        self.headers = {
            "Cookie": ""
        }

    def print_time(func):
        def wrapper(self):
            s_time = time.time()
            print("开始时间：{}".format(datetime.datetime.now().strftime("%X")))
            func(self)
            e_time = time.time()
            print("结束时间：{}".format(datetime.datetime.now().strftime("%X")))
            print("总耗时：{}".format(e_time - s_time))

        return wrapper

    def send_req(self):
        res = requests.post(url=self.req_url, json=self.req_data, headers=self.headers)
        print(res.json())

    def create_gevent(self):
        g_list = []
        for i in range(self.gevent_num):
            g = gevent.spawn(KKInterface().getRewardRecord)
            g_list.append(g)
        gevent.joinall(g_list)

    def create_task(self):

        for i in range(self.task_num):
            p = Process(target=self.create_gevent)
            p.start()
        p.join()

    @print_time
    def run(self):
        self.create_gevent()


if __name__ == '__main__':
    ApiTest().run()

