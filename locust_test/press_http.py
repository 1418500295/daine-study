import time

import requests,threading


class Press():

    ok = 0

    def http_send(self):
        data = {
            "name": "daine",
            "age": "26"
        }
        resp = requests.get("http://localhost:8889/v1/getDemo", params=data).json()
        print(resp)
        if resp["info"] == "success":
            self.ok += 1

    def run_script(self):
        i = 0
        num = 100
        s_time = time.time()
        while i < num:
            t = threading.Thread(target=self.http_send)
            t.setDaemon(True)
            t.start()
            i += 1
        t.join()
        e_time = time.time()
        print(self.ok)
        print(e_time - s_time)



if __name__ == '__main__':
    Press().run_script()














    





