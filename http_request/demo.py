

class Study():

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __run(self):
        print("hello")

    def sing(self):
        print("sing")

class Man(Study):

    def play(self):
        print("play")


    def drink(self):
        # super().sing()
        super(Man,self).sing()

    def sing(self):
        print("hha")
    



if __name__ == '__main__':
    s = Study("daine",12)
    s.sing()
    # 调用私有方法
    s._Study__run()

    m = Man("james",11)
    m.drink()
    m.sing()













3.获取telegram群组id：

  3.1先将机器人添加至对应telegram群组

  3.2 浏览器输入https://api.telegram.org/bot(机器人token)/getUpdates,获取telegram对应群组id


import json
import time

import requests
from jira import JIRA


class JiraTool:
    # 初始化
    def __init__(self):
        self.server = 'http://jira'
        self.basic_auth = ('glen', '123')
        self.token = '65:AAFQgPHsohM'
        # self.chat_id = 635  #机器人id
        # self.chat_id = -751  #工作组群组id
        self.chat_id = -980
        self.test_user = ['ro','ye','mac','mio']
        self.android_list = ['esid','aon','ter_id','ndr','jn']
        self.ios_list = ['fl','jin_ios','is','gin']
        self.pc_list = ['loo','so']
        self.otc_webList = ['xi_ob']
        self.back_list = ['am','ea','en','sng','an','le','da','in']
        self.product_list = ['bo','ok','d_ect']
        # self.bugList = []
        # self.bugForWho = []
        self.jiraClinet = None
        self.data = None

    def login(self):
        self.jiraClinet = JIRA(server=self.server, basic_auth=self.basic_auth)
        if self.jiraClinet != None:
            # print("登录成功！")
            return True
        else:
            return False

    def get_issue_list_by_jql(self, jql, testList,androidList,iosList,back_list,pcList,webList,productList):
        issue_list = []
        issue_key_list = self.jiraClinet.search_issues(jql_str=jql, startAt=0,
                                                     maxResults=1000)
        data_dict = {}
        for key_list in issue_key_list:
            issue = self.jiraClinet.issue(key_list.key)
            issue_list.append(issue)
            # print("单号: ",issue.key) #关键字
            # bugList.append(issue.key)
            # bugForWho.append(str(issue.fields.assignee))
            if str(issue.fields.assignee) in self.test_user:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                testList.append(self.data)
            elif str(issue.fields.assignee) in self.android_list:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                androidList.append(self.data)
            elif str(issue.fields.assignee) in self.ios_list:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                iosList.append(self.data)
            elif str(issue.fields.assignee) in self.back_list:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                back_list.append(self.data)
            elif str(issue.fields.assignee) in self.pc_list:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                pcList.append(self.data)
            elif str(issue.fields.assignee) in self.otc_webList:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                webList.append(self.data)
            elif str(issue.fields.assignee) in self.product_list:
                self.data = '%s-%s' % (issue.fields.assignee, issue.key)
                productList.append(self.data)
            # print(self.data)
            # print("bug描述: ",issue.fields.summary) #bug描述
            # print("bug状态: ",issue.fields.status) #bug状态
            # print("经办人: ",issue.fields.assignee) #经办人
            # print(issue.fields.components[0].name) #模块
            # print("优先级: ",issue.fields.priority) #优先级
            # print('***************************************************************')
        return issue_list

    def gen_new_bug_caption_str(issue_list):
        dict = {}
        for issue in issue_list:
            dict[issue.fields.status.name] = dict.get(issue.fields.status.name, 0) + 1
            # dict[issue.key.split('-')[0]] = dict.get(issue.key.split('-')[0],0) + 1
        caption_str = '近一周共计新增bug' + str(len(issue_list)) + '个。 已关闭：' + str(
            dict.get('已关闭')) + '个。 已解决待关闭：' + str(dict.get('已解决')) + '个。 待处理：' + str(
            dict.get('待处理')) + '个'
        # print(caption_str)
        return caption_str

    def send_telegram(self,content):
        r = requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage',
                          json={"chat_id": self.chat_id, "text":content})
        print(r)


if __name__ == '__main__':
    # 待回归bug
    new_bug_jql = "issuetype = Bug AND status in (\"Pending Test\", 待测试处理, 待测试) order by created DESC"
    # 待解决bug
    deal_bug_jql = 'issuetype = Bug AND status in (处理中, 待处理) order by created DESC'

    fix_jql = 'project = COIN68 AND issuetype = Improvement AND status in (需求确认, 处理中) order by created DESC'
    # old_bug_jql = "project in (AAA, BBB, CCC)  AND issuetype in (Bug, 缺陷) AND status in (待处理, 开发中, Reopened) AND created <= -1w ORDER BY component ASC, assignee ASC, priority DESC, updated DESC"
    jiraTool = JiraTool()
    jiraTool.login()

    testList = []
    android_list = []
    ios_list = []
    back_list = []
    pc_list = []
    web_list = []
    product_list = []

    new_issue_list = jiraTool.get_issue_list_by_jql(new_bug_jql,testList,android_list,ios_list,back_list,pc_list,web_list,product_list)
    # print(new_issue_list)
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("待测试bug总数：", len(new_issue_list))
    # print("待测试bug单号：", bugList)
    # print("当前经办人：", bugForWho)
    print("********************************************")
    testList1 = []
    android_list1 = []
    ios_list1 = []
    back_list1= []
    pc_list1 = []
    web_list1 = []
    product_list1 = []
    deal_bug_list = jiraTool.get_issue_list_by_jql(deal_bug_jql,testList1,android_list1,ios_list1,back_list1,pc_list1,web_list1,product_list1)
    # print(deal_bug_list)
    print("待处理、处理中bug总数：", len(deal_bug_list))
    print("**********************************************")
    testList2 = []
    android_list2 = []
    ios_list2 = []
    back_list2 = []
    pc_list2 = []
    web_list2 = []
    product_list2 = []
    fix_list = jiraTool.get_issue_list_by_jql(fix_jql,testList2,android_list2,ios_list2,back_list2,pc_list2,web_list2,product_list2)
    print("开启、处理中的改进单数：", len(fix_list))
    # print(fix_list)
    # print("待处理、处理中bug单号：",bugList1)
    # print("当前经办人：", bugForWho1)
    # print(new_bug_html)
    # old_issue_list = jiraTool.get_issue_list_by_jql(old_bug_jql)
    # print(old_issue_list)
    # print(eamil_html)
    # content = time.strftime("%Y-%m-%d %H:%M:%S")+" : "+\
    #           "\n"+'待回归bug总数：'+str(len(new_issue_list))+'\n'+"【测试】："+"\n"+json.dumps(testList)+\
    #           "\n"+'\n'+\
    #           "*******************************"+'\n'+"\n"+'待处理、处理中bug总数：'+str(len(deal_bug_list))+'\n'+"【测试】："+"\n"+\
    #           json.dumps(testList1)+"\n"+"【安卓】："+'\n'+json.dumps(android_list1)+"\n"+\
    #           "【IOS】: "+"\n"+json.dumps(ios_list1)+"\n"+"【后端】："+"\n"+json.dumps(back_list1)+"\n"+\
    #           "【PC】: "+"\n"+json.dumps(pc_list1)+"\n"+"【otc_web】: "+'\n'+json.dumps(web_list1)+"\n"+"【产品】: "+\
    #           "\n"+json.dumps(product_list1)+"\n"+'\n'+"************************************"+"\n"+"\n"+"开启、处理中的改进单数："+str(len(fix_list))+'\n'+"【测试】："+"\n"+\
    #           json.dumps(testList2)+"\n"+"【安卓】："+'\n'+json.dumps(android_list2)+"\n"+\
    #           "【IOS】: "+"\n"+json.dumps(ios_list2)+"\n"+"【后端】："+"\n"+json.dumps(back_list2)+"\n"+\
    #           "【PC】: "+"\n"+json.dumps(pc_list2)+"\n"+"【otc_web】: "+'\n'+json.dumps(web_list2)+"\n"+"【产品】: "+\
    #           "\n"+json.dumps(product_list2)

# '待测试bug单：' + '\n' + json.dumps(bugList) + "\n" \
    # +"待处理、处理中bug单号：" + '\n' + json.dumps(bugList1) + "\n"
    jiraTool.send_telegram("hello")



