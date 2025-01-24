import time
from datetime import datetime

import jenkins
import requests
from requests.auth import HTTPBasicAuth
jenkins_url = 'https://'
token="6jh4"
jenkins_username = 'ne'
jenkins_password = '34!'
chat_id = -4
# chat_id = 71
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
                                    "text": f'Job： {s["name"]}\n'
                                            f'分支：{s["分支"]}\n环境：{s["环境"]}\n服务：{s["服务"]}\n'
                                            f'java_depend是否勾选：{s["java_depend"]}\nBUILD_ID：{s["n"]}\n构建已完成：#{status}'})
            service_list.remove(s)
    for c1 in c:
        n = c1['number']
        name = c1['name']
        print("url: ",c1['url'])
        # print(n)
        # print(c1)
        if c1:
            if '68IOS' not in name:
                res = requests.get(c1['url'] + "/api/json", auth=HTTPBasicAuth(jenkins_username, jenkins_password))
                time_stamp = \
                requests.get(c1['url'] + "/api/json", auth=HTTPBasicAuth(jenkins_username, jenkins_password)).json()[
                    'timestamp']
                print("res ",res.json())
                # res = res.json()['actions'][0]['parameters']
                res = res.json()['actions']
                parameters = None
                l = []
                for i in res:
                    if 'parameters' in i:
                        parameters = i['parameters']
                print("s: ",parameters)
                branch = None
                env = None
                service = None
                java_depend_sel = None
                for r1 in parameters:
                    # print("r1: ",r1)
                    if r1['name'] == "Git_Tag":
                        branch = r1['value']
                    if r1['name'] == 'deploy_site':
                        env = r1['value']
                    if r1['name'] == 'SELECT_SITE':
                        service = r1['value']
                    try:
                        if r1['name'] == 'java_depend':
                            java_depend_sel = r1['value']
                    except:
                        pass
                build_start_time = str(datetime.fromtimestamp(time_stamp / 1000)).split('.')[0]
                # status = jk.get_build_info(name='e68_TEST.007.update_openchat', number=769)['result']
                if n not in n_list:
                    r = requests.post(telegram_bot_header,
                                      json={"chat_id": chat_id,
                                            "text": f'Job:  {c1["name"]}\n构建时间：{build_start_time}\n分支：{branch}\n环境：'
                                                    f'{env}\n服务：{service}\njava_depend是否勾选：'
                                                    f'{java_depend_sel}\nBUILD_ID：{c1["number"]}\n#构建中'})
                    # r = requests.post(telegram_bot_header,
                    #                   json={"chat_id": chat_id, "text": f'{c1["name"]}\n构建时间：{build_start_time}\nBUILD_ID：{c1["number"]}\n#构建中'})
                n_list.add(n)
                service_map["name"] = name
                service_map['n'] = n
                service_map['分支'] = branch
                service_map['环境'] = env
                service_map['服务'] = service
                service_map["java_depend"] = java_depend_sel
                service_list.append(service_map)
                service_list = [dict(t) for t in set([tuple(d.items()) for d in service_list])]
    print("service_list: ",service_list)
    print('n_list: ',n_list)
    time.sleep(10)



