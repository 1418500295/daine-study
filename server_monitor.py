import psutil
import time
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import os
from datetime import datetime

# ================== 配置部分 ==================
MONITOR_INTERVAL = 1  # 监控间隔（秒）
EXCEL_FILE = "server_monitor.xlsx"
CHART_IMG = "temp_chart.png"


# ================== 监控功能 ==================
class ServerMonitor:
    def __init__(self):
        self.data = []
        self.last_net = psutil.net_io_counters()
        self.last_time = time.time()

    def collect_metrics(self):
        """采集性能指标"""
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # CPU 使用率
        cpu_percent = psutil.cpu_percent()

        # 内存使用率
        mem_percent = psutil.virtual_memory().percent

        # 磁盘使用率（默认根目录）
        disk_percent = psutil.disk_usage('/').percent

        # 网络速度计算（KB/s）
        current_net = psutil.net_io_counters()
        elapsed = time.time() - self.last_time
        net_sent = (current_net.bytes_sent - self.last_net.bytes_sent) / elapsed / 1024
        net_recv = (current_net.bytes_recv - self.last_net.bytes_recv) / elapsed / 1024

        # 更新基准值
        self.last_net = current_net
        self.last_time = time.time()

        return {
            "时间": now,
            "CPU使用率(%)": cpu_percent,
            "内存使用率(%)": mem_percent,
            "磁盘使用率(%)": disk_percent,
            "网络上传(KB/s)": round(net_sent, 2),
            "网络下载(KB/s)": round(net_recv, 2)
        }

    def generate_chart(self, df):
        """生成监控图表"""
        plt.figure(figsize=(14, 10))
        plt.rcParams['font.family'] = ['SimHei']  # 指定中文字体为黑体


        # 转换时间格式
        df['时间'] = pd.to_datetime(df['时间'])

        # CPU 图表
        plt.subplot(2, 2, 1)
        plt.plot(df['时间'], df['CPU使用率(%)'], 'r-', label='CPU')
        plt.title('CPU USE')
        plt.xticks(rotation=30)
        plt.grid(True)

        # 内存图表
        plt.subplot(2, 2, 2)
        plt.plot(df['时间'], df['内存使用率(%)'], 'b-', label='Memory')
        plt.title('MEMORY USE')
        plt.xticks(rotation=30)
        plt.grid(True)

        # 磁盘图表
        plt.subplot(2, 2, 3)
        plt.plot(df['时间'], df['磁盘使用率(%)'], 'g-', label='Disk')
        plt.title('DISK USE')
        plt.xticks(rotation=30)
        plt.grid(True)

        # 网络图表
        plt.subplot(2, 2, 4)
        plt.plot(df['时间'], df['网络上传(KB/s)'], 'orange', label='Upload')
        plt.plot(df['时间'], df['网络下载(KB/s)'], 'purple', label='Download')
        plt.title('NET SPEED')
        plt.legend()
        plt.xticks(rotation=30)
        plt.grid(True)

        plt.tight_layout()
        plt.savefig(CHART_IMG, dpi=150, bbox_inches='tight')
        plt.close()

    def save_to_excel(self):
        """保存数据到Excel并插入图表"""
        df = pd.DataFrame(self.data)

        # 保存数据到Excel
        df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

        # 生成图表
        self.generate_chart(df)

        # 将图表插入Excel
        wb = load_workbook(EXCEL_FILE)
        ws = wb.active
        img = Image(CHART_IMG)
        img.anchor = 'A' + str(len(df) + 3)  # 图表插入位置
        ws.add_image(img)
        wb.save(EXCEL_FILE)

        # 清理临时文件
        if os.path.exists(CHART_IMG):
            os.remove(CHART_IMG)

    def run(self):
        """主监控循环"""
        try:
            print("🖥️ 服务端监控启动中... (按 Ctrl+C 停止)")
            print(f"数据将保存到: {os.path.abspath(EXCEL_FILE)}")
            while True:
                metrics = self.collect_metrics()
                self.data.append(metrics)
                print(
                    f"[{metrics['时间']}] "
                    f"CPU: {metrics['CPU使用率(%)']}% | "
                    f"内存: {metrics['内存使用率(%)']}% | "
                    f"磁盘: {metrics['磁盘使用率(%)']}% | "
                    f"网络: ↑{metrics['网络上传(KB/s)']}KB/s ↓{metrics['网络下载(KB/s)']}KB/s"
                )
                time.sleep(MONITOR_INTERVAL)
        except KeyboardInterrupt:
            print("\n正在保存数据...")
            self.save_to_excel()
            print(f"✅ 数据与图表已保存到 {EXCEL_FILE}")


# ================== 主程序 ==================
if __name__ == "__main__":
    monitor = ServerMonitor()
    monitor.run()
