import asyncio
import json
import time

ios抓包工具：Hodor  surge
import requests
from jira import JIRA

jira_server = 'http://jira./'
user_name = 'cnt'
password = '1x'

jira = JIRA(basic_auth=(user_name, password), options={'server': jira_server})

a = 1
b = 1
c = 1
d = 1
e = 1
first_coin = ""
android_list = []
ios_list = []
otc_list = []
pc_list = []
fwd_list = []
version = "V0"
link = 'http://j'
android_bug_jql = f"project =  AND issuetype = Bug AND component = Android AND status in (处理中, 待处理) AND fixVersion = {version} order by created DESC"
ios_bug_jql = f"project =  AND issuetype = Bug AND component = iOS AND status in (处理中, 待处理) AND fixVersion = {version} order by created DESC"
otc_bug_jql = f"project =  AND issuetype = Bug AND component = OTC后台 AND status in (处理中, 待处理) AND fixVersion = {version} order by created DESC"
fwd_bug_jql = f"project =  AND issuetype = Bug AND component = 服务端 AND status in (处理中, 待处理) AND fixVersion = {version} order by created DESC"
pc_bug_jql = f"project =  AND issuetype = Bug AND component = PC桌面端 AND status in (处理中, 待处理) AND fixVersion = {version} order by created DESC"

jira_list = []


def get_jira_bug(bug_jql, amount, summary_list):
    for u in jira.search_issues(bug_jql):
        version = jira.issue(u).raw['fields']['fixVersions'][0]['name']
        jira_list.append(str(u))
        summary = jira.issue(u).fields.summary
        complete_data = str(
            amount) + ". " + f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --" + version + "                "
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
            summary_list.append(
                str(amount) + ". " + f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --" + version + "                " + summary + "\n")
        amount += 1


import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, Updater, CallbackContext, ContextTypes

get_jira_bug(android_bug_jql, a, android_list)
get_jira_bug(ios_bug_jql, b, ios_list)
get_jira_bug(otc_bug_jql, c, otc_list)
get_jira_bug(fwd_bug_jql, d, fwd_list)
get_jira_bug(pc_bug_jql, e, pc_list)

# print(cont_list)
chat_id = 7170293249
token = "6903033642:AAHJU4nxGHeW_96pYavCqe2UsQKJMqv7jh4"
application = ApplicationBuilder().token(token).build()

bot = telegram.Bot(token=token)
bug_title = f"===================" + f'<a href="{link}{jira_list[0]}?filter=-4&jql=status%20in%20(%E5%A4%84%E7%90%86%E4%B8%AD%2C%20%E5%BE%85%E5%A4%84%E7%90%86)%20AND%20fixVersion%20%3D%20{version}%20order%20by%20created%20DESC">{version}版本待解决bug</a>' + "===================\n"
bug_time = time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime())


async def start():
    await bot.send_message(chat_id=chat_id, text=bug_title + time.strftime("%Y-%m-%d %H:%M:%S\n",
                                                                           time.localtime()) + "安卓:" + "\n" + "".join(
        android_list) + "\n"
                                                 + "ios:" + "\n" + "".join(ios_list) + "\n"
                                                 + "otc后台:" + "\n" + "".join(otc_list) + "\n"
                                                 + "服务端:" + "\n" + "".join(fwd_list) + "\n"
                                                 + "pc端:" + "\n" + "".join(pc_list), parse_mode="HTML")
async def png():
    await bot.send_photo(chat_id=chat_id, photo=open("./bug.png","rb"))
    
import matplotlib.pyplot as plt

sizes = [len(android_list), len(ios_list), len(otc_list), len(fwd_list),len(pc_list)]

plt.rcParams['font.family'] = ['SimHei']  # 指定中文字体为黑体
labels = [an, ios, otc, fwd,pc]
plt.bar(x=labels,height=sizes)
for a,b in zip(labels, sizes):
    plt.text(a,b,
             b,
             ha='center',
             va='bottom',
            )
plt.title("各端bug数量")
plt.savefig("./bug.png")

loop = asyncio.get_event_loop()
loop.run_until_complete(start())

# r = requests.post(f'https://api.telegram.org/bot{token}/sendMessage',
#                   json={"chat_id": chat_id, "text":"===================="+version+"版本待解决bug====================\n"+"安卓:"+"\n" + "".join(android_list)+"\n"
#                         +"ios:"+"\n"+"".join(ios_list)+"\n"
#                         +"otc后台:"+"\n"+"".join(otc_list)+"\n"
#                         +"服务端:"+"\n"+"".join(fwd_list)+"\n"
#                         +"pc端:"+"\n"+"".join(pc_list)})
