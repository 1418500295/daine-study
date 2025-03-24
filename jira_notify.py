import os
import json
import logging
from jira import JIRA
import requests
import datetime
import pytz
import time
from typing import Dict, Optional

from pymysql.converters import escape_str

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('jira_monitor.log'),
        logging.StreamHandler()
    ]
)

# 配置参数（通过环境变量注入）
CONFIG = {
    'STATE_FILE': 'jira_monitor_state.json'  # 新增状态存储文件
}

# 初始化Jira客户端
JIRA_SERVER = 'http:'
JIRA_USER = ''
JIRA_PASSWORD = ''
TELEGRAM_TOKEN = ':'
TELEGRAM_CHAT_ID = '-'
# TELEGRAM_CHAT_ID = ''

JIRA_PROJECT = ''


# 初始化Jira客户端

TIMEZONE = 'Asia/Shanghai'
class StateManager:
    """状态持久化管理器"""

    def __init__(self):
        self.state_file = CONFIG["STATE_FILE"]
        self.last_check = self._load_initial_state()

    def _load_initial_state(self) -> datetime.datetime:
        """加载初始状态"""
        try:
            with open(self.state_file, 'r') as f:
                data = json.load(f)
                return datetime.datetime.fromisoformat(data["last_check"]).astimezone(pytz.utc)
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            return datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=1)

    def save_checkpoint(self, timestamp: datetime.datetime):
        """保存检查点"""
        data = {
            "last_check": timestamp.isoformat(),
            "saved_at": datetime.datetime.now(pytz.utc).isoformat()
        }
        with open(self.state_file, 'w') as f:
            json.dump(data, f)


class JiraWatcher:
    """Jira监控核心类"""

    def __init__(self):
        self.state = StateManager()
        self.tz = pytz.timezone(TIMEZONE)
        self.jira = self._init_jira_client()

    def _init_jira_client(self) -> JIRA:
        """初始化Jira客户端"""
        return JIRA(basic_auth=(JIRA_USER, JIRA_PASSWORD), options={'server': JIRA_SERVER})


    def _build_query(self) -> str:
        """构建监控查询语句"""
        check_time = self.state.last_check.astimezone(self.tz)
        time_filter = check_time.strftime("%Y-%m-%d %H:%M")
        return (
            f'project = {JIRA_PROJECT} '
            f'AND (updated >= "{time_filter}" OR created >= "{time_filter}") '
            'ORDER BY created ASC, updated ASC'
        )

    def _parse_timestamp(self, jira_time: str) -> datetime.datetime:
        """解析Jira时间戳"""
        try:
            return datetime.datetime.strptime(jira_time, "%Y-%m-%dT%H:%M:%S.%f%z").astimezone(pytz.utc)
        except ValueError:
            return datetime.datetime.strptime(jira_time, "%Y-%m-%dT%H:%M:%S%z").astimezone(pytz.utc)

    def _detect_changes(self):
        """执行变更检测"""
        jql = self._build_query()
        issues = self.jira.search_issues(
            jql,
            expand='changelog',
            # fields='key,summary,issuetype,created',
            maxResults=100
        )

        current_max = self.state.last_check
        for issue in issues:
            # 处理新建工单
            created_time = self._parse_timestamp(issue.fields.created)
            if created_time > self.state.last_check:
                self._notify_creation(issue, created_time)
                current_max = max(current_max, created_time)

            # 处理更新记录
            if hasattr(issue, 'changelog'):
                for history in issue.changelog.histories:
                    history_time = self._parse_timestamp(history.created)
                    if history_time > self.state.last_check:
                        self._notify_updates(issue, history)
                        current_max = max(current_max, history_time)

        # 更新检查点
        if current_max > self.state.last_check:
            self.state.last_check = current_max
            self.state.save_checkpoint(current_max)
            logging.info(f"检查点更新至：{current_max.isoformat()}")

    def _notify_creation(self, issue, created_time: datetime.datetime):
        """通知工单创建"""
        s = None
        local_time = created_time.astimezone(self.tz).strftime("%Y-%m-%d %H:%M:%S")
        c =  str(issue.fields.assignee).strip()
        # print(c)
        if c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 产品
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 后端开发
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 安卓
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '-akon':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 前端
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == 'jon':
            s = '@'
        elif c == '':
            s = '@'
        # ios
        elif c == 'blink':
            s = '@'
        elif c == 'five_68':
            s = '@'
        elif c == 'jackchen':
            s = '@'
        elif c == 'jack':
            s = '@'
        else:
            s = c
        message = [
            "🚨 *新建工单通知*",
            f"🔧 类型：{issue.fields.issuetype.name}",
            f"🏷 编号：{issue.key}",
            f"🔗 链接：{JIRA_SERVER}browse/{issue.key}",
            f"📝 标题：{issue.fields.summary}",
            f"🕒 创建时间：{local_time}",
            f"👤 创建人：{issue.fields.creator.displayName}\n"
            f"👤 经办人：{s}\n"
        ]
        self._send_telegram('\n'.join(message))

    def _notify_updates(self, issue, history):
        """通知字段更新"""
        s = None
        local_time = self._parse_timestamp(history.created).astimezone(self.tz).strftime("%Y-%m-%d %H:%M:%S")
        c = str(issue.fields.assignee).strip()
        ceshi_report_list = ['yihuik','clement','rose','eshine']
        if c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 产品
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 后端开发
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 安卓
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # 前端
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        # ios
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        elif c == '':
            s = '@'
        else:
            s = c
        for item in history.items:
            types = str(issue.fields.issuetype.name).strip()
            new_value = str(item.toString).strip()
            message = [
                "🔄 *字段更新通知*",
                f"🔧 类型：{issue.fields.issuetype.name}",
                f"🏷 编号：{issue.key}",
                f"🔗 链接：{JIRA_SERVER}browse/{issue.key}",
                f"📝 标题：{issue.fields.summary}",
                f"📌 字段：{item.field}",
                f"⬅ 旧值：`{item.fromString or '无'}`",
                f"➡ 新值：`{item.toString or '无'}`",
                f"🕒 修改时间：{local_time}",
                f"👤 修改人：{history.author.displayName}\n"
                f"👤 经办人：{s}\n"
            ]
            if types == "故障" and new_value == "完成":
                pass
            elif types == "故障" and new_value == "Done":
                pass
            elif types == "故障" and '修复.png' in new_value:
                pass
            elif types == '故障' and c in ceshi_report_list and '待测试' not in str(item.toString).strip():
                pass
            elif str(history.author.displayName).strip() in s.lower():
                pass
            elif str(history.author.displayName).strip() == "yo" and s == '@6688':
                pass
            else:
                self._send_telegram('\n'.join(message))

    def _send_telegram(self, message: str):
        """发送Telegram通知"""
        try:
            response = requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                json={
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": message,
                    # "parse_mode": "Markdown",
                    "disable_web_page_preview": True
                },
                timeout=10
            )
            response.raise_for_status()
        except Exception as e:
            logging.error(f"消息发送失败：{str(e)}")

    def run_service(self):
        """运行监控服务"""
        logging.info(f"启动Jira监控服务，项目：{JIRA_PROJECT}")
        try:
            while True:
                try:
                    self._detect_changes()
                    time.sleep(10)
                except requests.exceptions.RequestException as e:
                    logging.warning(f"网络错误：{str(e)}，30秒后重试")
                    time.sleep(30)
                except Exception as e:
                    logging.error(f"运行时错误：{str(e)}")
                    time.sleep(60)
        except KeyboardInterrupt:
            logging.info("收到中断信号，保存状态后退出")
            self.state.save_checkpoint(self.state.last_check)


if __name__ == "__main__":
    watcher = JiraWatcher()
    watcher.run_service()
