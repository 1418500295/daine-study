import time
from datetime import datetime

import jenkins
import requests
from requests.auth import HTTPBasicAuth
jenkins_url = 'https://jenkins'
token="642:AAHJU4nxGHeW_"
jenkins_username = 'ye'
jenkins_password = '34!'
# chat_id = -467
chat_id = 717
telegram_bot_header = f'https://api.telegram.org/bot{token}/sendMessage'
jk = jenkins.Jenkins(url=jenkins_url, username=jenkins_username, password=jenkins_password)
n_list = set()
service_map = dict()
service_list = list()
while True:
    c = jk.get_running_builds()
    print(c)
    print(time.strftime("%H:%M:%S",time.localtime()))
    for s in service_list:
        status = jk.get_build_info(name=s['name'], number=s['n'])['result']
        print(status)
        if status is not None:
            r = requests.post(telegram_bot_header,
                              json={"chat_id": chat_id,
                                    "text": f'{s["name"]}\nBUILD_ID：{s["n"]}\n构建已完成：#{status}'})
            service_list.remove(s)
    for c1 in c:
        n = c1['number']
        name = c1['name']
        # print("url: ",c1['url'])
        build_timestamp = requests.get(c1['url']+"/api/json",auth=HTTPBasicAuth(jenkins_username, jenkins_password)).json()['timestamp']
        build_start_time = str(datetime.fromtimestamp(build_timestamp/1000)).split('.')[0]
        print(n)
        print(c1)
        if c1:
            # status = jk.get_build_info(name='e68_TEST.007.update_openchat', number=769)['result']
            if n not in n_list:
                r = requests.post(telegram_bot_header,
                                  json={"chat_id": chat_id, "text": f'{c1["name"]}\n构建时间：{build_start_time}\nBUILD_ID：{c1["number"]}\n#构建中'})
            n_list.add(n)
            service_map["name"] = name
            service_map['n'] = n
            service_list.append(service_map)
            service_list = [dict(t) for t in set([tuple(d.items()) for d in service_list])]
    print("service_list: ",service_list)
    print('n_list: ',n_list)
    time.sleep(10)



