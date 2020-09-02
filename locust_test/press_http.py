import time

import requests,threading


class Press():

    num = 0
    ok = 0


    def http_send(self):
        # data = {
        #     "name": "daine",
        #     "age": "26"
        # }
        resp = requests.get("https://www.baidu.com").content.decode('utf-8')
        print(resp)
        if "百度一下" in resp:
            self.ok += 1

    def run(self):
        print(time.strftime("%Y-%m-%d : %H-%M-%S", time.localtime()))
        while self.num < 500:

            t = threading.Thread(target=self.http_send)
            t.setDaemon(True)
            t.start()
            self.num+=1
        t.join()
        e_time = time.time()
        print(self.ok)
        print(time.strftime("%Y-%m-%d : %H-%M-%S", time.localtime()))

    # def run_script(self):
    #     i = 0
    #     s_time = time.time()
    #     while i < num:
    #         t = threading.Thread(target=self.http_send)
    #         t.setDaemon(True)
    #         t.start()
    #         i += 1
    #     t.join()
    #     e_time = time.time()
    #     print(self.ok)
    #     print(e_time - s_time)



if __name__ == '__main__':
    Press().run()














    





