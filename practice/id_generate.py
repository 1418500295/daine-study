
import paramiko
import json
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect("127.0.0.1",8788,'root','111111')
#
# stdin, stodut, stder = ssh.exec_command('ls -al')
#
# # 将byte转换为字符串
# # print((str((stodut.read()),'utf-8')))
# print(stodut.read().decode('utf-8'))
#
# ssh.close()




# # 上传和下载文件  SFTPClient
#
# transport = paramiko.Transport("127.0.0.1",8788)
# transport.connect('root','111111')
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# sftp.put("climb.py","/a.py")
#
# transport.close()

import requests,os

# rs = requests.get("https://www.baidu.com")
# # print(rs.content.decode('utf-8'))
# print(str(rs.content,'utf-8'))
# # rs.encoding='utf-8'
# # print(rs.text)


def run_main():
    method = input("请求方式是:")
    if method == 'get':
        params = input("请输入请求地址:")
        rs = requests.get(params)
        print(rs.json())
    elif method == 'post':
        url = input("请输入url:")
        data = input("请输入请求体:")
        rs = requests.post(url,data=data)
        print(rs.json())
if __name__ == '__main__':
    run_main()
    os.system("pause")
    # rs = requests.post("http://localhost:8889/postSecond",{"name":"daine","sex":"male"})
    # print(rs.json())




