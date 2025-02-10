
import asyncio
import sys
import time
from typing import Any
import requests
from jira import JIRA
import telegram
from matplotlib.ticker import MaxNLocator

from utils.random_account import random_str
from utils.send_result import chat_id
jira_list = []
keyword = '交'
jira_server = 'https://l.com/'
user_name = 'ct'
password = ''
jira = JIRA(basic_auth=(user_name, password), options={'server': jira_server})
android_list = []
ios_list = []
otc_list = []
pc_list = []
fwd_list = []
fwd_list1 = []
status = ('处理中', '待处理')
pindao_list = []
a = 1
b = 1
c = 1
d = 1
e = 1
ios_content_list = []
android_content_list = []

fwd_content_list = []
link = 'http://jira.esccall.com/browse/'
bot = telegram.Bot(token="642:Av7jh4")
android_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in {status} AND Summary ~ '\"{keyword}\"' order by created DESC"
ios_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in {status}   AND Summary ~ '\"【ios】\"' AND Summary !~ '\"【otc】\"' AND Summary !~ '\"【服务端】\"' AND Summary !~ '\"【安卓】\"' AND Summary ~ '\"{keyword}\"'  order by created DESC"
otc_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in {status}  AND Summary ~ '\"【otc】\"' AND Summary ~ '\"{keyword}\"' AND Summary !~ '\"【服务端】\"' AND Summary !~ '\"【安卓】\"' AND Summary !~ '\"【ios】\"' order by created DESC"
fwd_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in {status}  AND Summary !~ '\"【安卓】\"' AND Summary !~ '\"【ios】\"' AND Summary ~ '\"{keyword}\"' AND Summary !~ '\"【otc】\"' order by created DESC"
# fwd_bug_jql1 = f"project = COIN68 AND issuetype = Bug AND status in ('Pending Test', 待测试)  AND Summary ~ '升级' order by created DESC"

def get_jira_bug(bug_jql, amount, summary_list):
    for u in jira.search_issues(bug_jql, maxResults=-1):
        # version = jira.issue(u).raw['fields']['fixVersions'][0]['name']
        jira_list.append(str(u))
        summary = jira.issue(u).fields.summary
        complete_data = f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --"
        if "<=" in summary:
            f = summary.replace("<=", "&le;")
            summary_list.append(
                complete_data + f + "\n")
        elif "<" in summary:
            f = summary.replace("<", "&lt;")
            summary_list.append(
                complete_data + f + "\n")
        elif ">" in summary:
            f = summary.replace(">", "&gt;")
            summary_list.append(
                complete_data + f + "\n")
        elif ">=" in summary:
            f = summary.replace(">=", "&ge;")
            summary_list.append(
                complete_data + f + "\n")
        else:
            summary_list.append(f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --" + summary + "\n")
        amount += 1
sum_list = []
get_jira_bug(android_bug_jql, a, sum_list)
for i in sum_list:
    x = i[0:100]
    if "安卓" in x:
        android_list.append(i)
    elif "IOS" in x or "ios" in x or "IOS" in x or "iOS" in x:
        ios_list.append(i)
    elif "服务端" in x:
        fwd_list.append(i)
    elif "otc" in x or 'OTC' in x or "Otc" in x:
        otc_list.append(i)
android_list1 = []
[android_list1.append(str(android_list.index(i)+1)+"."+i) for i in android_list]
ios_list1 = []
[ios_list1.append(str(ios_list.index(i)+1)+"."+i) for i in ios_list]
fwd_list1 = []
[fwd_list1.append(str(fwd_list.index(i)+1)+"."+i) for i in fwd_list]
x = 1
y = 1
otc_qianduan =[]
otc_houduan = []
for i in otc_list:
    i1 = str(i).split('</a>')[0].split(">")[1]
    handler = jira.issue(i1).fields.assignee
    if str(handler).startswith("hao"):
        otc_qianduan.append(str(x) + ". <a" + str(i).split("<a")[1])
        x += 1
    else:
        otc_houduan.append(str(y) + ". <a" + str(i).split("<a")[1])
        y += 1
# chat_id = 7170
# await bot.send_message(chat_id=chat_id, text="""<code>是否是刚好</code>""",parse_mode="HTML")
async def start0():
    await bot.send_message(chat_id=chat_id, text=f"==================={keyword}功能待解决BUG:===================\n")
async def start(mode="安卓", bug_l=[]):
    if bug_l is None:
        bug_l = []
    await bot.send_message(chat_id=chat_id, text=mode + ":\n" + "".join(
        bug_l) + "\n"
                           , parse_mode="HTML")
async def png():
    await bot.send_photo(chat_id=chat_id, photo=open("./bug.png", "rb"))
# import mplcyberpunk

import matplotlib.pyplot as plt
sizes = [len(android_list), len(ios_list), len(otc_qianduan), len(otc_houduan),len(fwd_list)]
an = "Android"
ios = 'IOS'
otc = 'OTC后台'
fwd = '服务端'
pc = 'PC端'

# plt.style.use("cyberpunk")
plt.rcParams['font.family'] = ['SimHei']  # 指定中文字体为黑体
labels = [an, ios, "OTC后台(前端)","OTC后台(后端)", fwd]
bar = plt.bar(x=labels, height=sizes, color=['#a2653e', '#b9a281', '#808080', '#658cbb',"darkcyan"])
# mplcyberpunk.add_bar_gradient(bars=bar)
plt.legend(loc="upper right",frameon=False)
# 设置显示整数
for a, b in zip(labels, sizes):
    plt.text(a, b,
             b,
             ha='center',
             va='bottom',
             )
plt.title(f"{keyword}功能待解决bug总计: {(len(android_list)+len(ios_list)+len(otc_qianduan)+len(otc_houduan)+len(fwd_list))}")
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig("./bug.png")
loop = asyncio.get_event_loop()
loop.run_until_complete(start0())
loop.run_until_complete(start("安卓", android_list1))
loop.run_until_complete(start("ios", ios_list1))
loop.run_until_complete(start("otc后台(前端)", otc_qianduan))
loop.run_until_complete(start("otc后台(后端)", otc_houduan))
loop.run_until_complete(start("服务端", fwd_list1))
loop.run_until_complete(png())
loop.stop()

# r = requests.post(f'https://api.telegram.org/bot{token}/sendMessage',
#                   json={"chat_id": chat_id, "text":"===================="+version+"版本待解决bug====================\n"+"安卓:"+"\n" + "".join(android_list)+"\n"
#                         +"ios:"+"\n"+"".join(ios_list)+"\n"
#                         +"otc后台:"+"\n"+"".join(otc_list)+"\n"
#                         +"服务端:"+"\n"+"".join(fwd_list)+"\n"
#                         +"pc端:"+"\n"+"".join(pc_list)})
