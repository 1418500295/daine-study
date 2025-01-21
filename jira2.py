import asyncio
import time
import requests
from jira import JIRA
import telegram
from matplotlib.ticker import MaxNLocator
from utils.send_result import chat_id
jira_list = []
keyword = '区'
jira_server = 'https:/l.com/'
user_name = 'ct'
password = '1qx'
jira = JIRA(basic_auth=(user_name, password), options={'server': jira_server})
android_list = []
ios_list = []
otc_list = []
pc_list = []
fwd_list = []
fwd_list1 = []

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
bot = telegram.Bot(token="6903033642:AAHJU4nxGHeW_96pYavCqe2UsQKJMqv7jh4")
android_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in (处理中, 待处理) AND Summary ~ '\"【安卓】\"' AND Summary !~ '\"【otc】\"' AND Summary !~ '\"【服务端】\"' AND Summary !~ '\"【ios】\"' AND Summary ~ '\"交易区\"' order by created DESC"
ios_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in (处理中, 待处理)   AND Summary ~ '\"【ios】\"' AND Summary !~ '\"【otc】\"' AND Summary !~ '\"【服务端】\"' AND Summary !~ '\"【安卓】\"' AND Summary ~ '\"交易区\"'  order by created DESC"
otc_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in (处理中, 待处理)  AND Summary ~ '\"【otc】\"' AND Summary ~ '\"交易区\"' AND Summary !~ '\"【服务端】\"' AND Summary !~ '\"【安卓】\"' AND Summary !~ '\"【ios】\"' order by created DESC"
fwd_bug_jql = f"project = COIN68 AND issuetype = Bug AND status in (处理中, 待处理)  AND Summary !~ '\"【安卓】\"' AND Summary !~ '\"【ios】\"' AND Summary ~ '\"交易区\"' AND Summary !~ '\"【otc】\"' order by created DESC"
# fwd_bug_jql1 = f"project = COIN68 AND issuetype = Bug AND status in ('Pending Test', 待测试)  AND Summary ~ '服务升级' order by created DESC"

def get_jira_bug(bug_jql, amount, summary_list):
    for u in jira.search_issues(bug_jql, maxResults=-1):
        # version = jira.issue(u).raw['fields']['fixVersions'][0]['name']
        jira_list.append(str(u))
        summary = jira.issue(u).fields.summary
        complete_data = str(
            amount) + ". " + f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --"
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
                str(amount) + ". " + f'<a href="{link}{str(u)}">{str(u)}</a>' + "       --" + summary + "\n")
        amount += 1

otc_qianduan = []
otc_houduan = []
get_jira_bug(android_bug_jql, a, android_list)
get_jira_bug(ios_bug_jql, b, ios_list)
get_jira_bug(otc_bug_jql, c, otc_list)
get_jira_bug(fwd_bug_jql, d, fwd_list)

# for i in ios_list:
#     if "安卓" in i:
#         ios_list.remove(i)
# for i in android_list:
#     if "【ios】" or "【IOS】" in i:
#         android_list.remove(i)
x = 1
y = 1
for i in otc_list:
    i1 = str(i).split('</a>')[0].split(">")[1]
    handler = jira.issue(i1).fields.assignee
    if str(handler).startswith("xiehao"):
        otc_qianduan.append(str(x) + ". <a" + str(i).split("<a")[1])
        x += 1
    else:
        otc_houduan.append(str(y) + ". <a" + str(i).split("<a")[1])
        y += 1
# chat_id = -92
chat_id = 71
# chat_id = -472

async def start():
    await bot.send_message(chat_id=chat_id, text=f"{keyword}功能待解决BUG:\n"
                                                 + "安卓:" + "\n" + "".join(
        android_list) + "\n"


        #                                          + "PC桌面端:" + "\n" + "".join(pc_list)
                           , parse_mode="HTML")
async def start1():
    await bot.send_message(chat_id=chat_id, text="ios:" + "\n" + "".join(ios_list) + "\n"

        #                                          + "PC桌面端:" + "\n" + "".join(pc_list)
                           , parse_mode="HTML")
async def start2():
    await bot.send_message(chat_id=chat_id, text="otc后台(前端):" + "\n" + "".join(otc_qianduan) + "\n"


        #                                          + "PC桌面端:" + "\n" + "".join(pc_list)
                           , parse_mode="HTML")
async def start3():
    await bot.send_message(chat_id=chat_id, text="otc后台(后端):" + "\n" + "".join(otc_houduan) + "\n"



        #                                          + "PC桌面端:" + "\n" + "".join(pc_list)
                           , parse_mode="HTML")
async def start4():
    await bot.send_message(chat_id=chat_id, text="服务端:" + "\n" + "".join(fwd_list) + "\n"

        #                                          + "PC桌面端:" + "\n" + "".join(pc_list)
                           , parse_mode="HTML")

async def png():
    await bot.send_photo(chat_id=chat_id, photo=open("./bug.png", "rb"))

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
loop.run_until_complete(start())
loop.run_until_complete(start1())
loop.run_until_complete(start2())
loop.run_until_complete(start3())
loop.run_until_complete(start4())
# loop.run_until_complete(start3())
# loop.run_until_complete(start())
loop.run_until_complete(png())


