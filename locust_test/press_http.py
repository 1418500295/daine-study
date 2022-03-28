import gevent
from gevent import monkey

# monkey.patch_all()
monkey.patch_socket()

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
            print("最小响应时间：", min(KKInterfaces().req_time))
            print("最大响应时间：", max(KKInterfaces().req_time))
            print("平均响应时间：", numpy.mean(KKInterfaces().req_time))
            print("成功的请求数：", len(KKInterfaces().success))
            print("失败的请求数: ", ApiTest().gevent_num - len(KKInterfaces().success))
            print("QPS: ", ApiTest().gevent_num / numpy.mean(KKInterfaces().req_time))
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
    
    
    
    
    
    
    
    
    def decorator(args="执行压测"):
        def wrapper(funcName):
            def func(self):
                sTime = time.time()
                s_time = self.format_time()
                funcName(self)
                eTime = time.time()
                e_time = self.format_time()
                print(self.resp_time)
                print(f'开始时间：{s_time}')
                print(f'结束时间：{e_time}')
                print(f'总耗时：{(lambda : eTime - sTime) ()}')
                print(f'最大响应时间：{max(self.resp_time)}')
                print(f'最小响应时间：{min(self.resp_time)}')
                print(f'50%用户响应时间：{(lambda res_time: res_time[int(len(res_time) * 0.5) - 1])(self.resp_time)}')
                print(f'90%用户响应时间：{(lambda res_time: res_time[int(len(res_time) * 0.9) - 1])(self.resp_time)}')
                print(f'平均响应时间：{numpy.mean(self.resp_time)}')
                print(f'QPS: {self.thread_num / numpy.mean(self.resp_time)}')
                print(f'总请求数：{self.thread_num}')
                print(f'成功的请求数: {self.success_num}')
                print(f'失败的请求数：{self.thread_num - self.success_num}')
            return func
        return wrapper

    @decorator()
    def run(self):
        req_list = []
        for i in range(self.thread_num):
            req_list.append(grequests.post(self.host+self.entrust_open_url,json=self.get_data(),
                                           headers={"x-token":self.getToken(i)}))
        res_list = grequests.map(req_list)
        for one in res_list:
            if isinstance(one.json(), dict):
                print(f'响应结果：{one.json()}')
                if one.json()['code'] == 200 and one.json()['data']['id']:
                    self.success_num += 1
            self.resp_time.append(one.elapsed.total_seconds())


if __name__ == '__main__':
    ApiTest().run()

