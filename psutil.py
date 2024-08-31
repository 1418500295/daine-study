import psutil
import time
import datetime

# run_time = 50
cpu = []
memory = []
disk = []
times = []
# print("当前日期     时间          CPU使用率 内存使用率 磁盘使用率")
s = time.time()
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.ticker as ticker


class Monitor():
    def interval(self, i):
        intervst = None
        if 0 <= i <= 300:
            intervst = 11
        elif 300 < i <= 600:
            intervst = 16
        elif 600 < i:
            intervst = 21
        return intervst

    def paint(self,example_cpu,intervst):
        plt.rcParams['font.family'] = 'SimHei'
        fig = plt.figure(figsize=(20, 7))
        ax = fig.add_subplot(111)
        plt.xticks(rotation=45, fontsize=13)
        plt.yticks(fontsize=13)
        if example_cpu == "cpu":
            plt.plot(times, cpu, color='red', label=example_cpu)
        elif example_cpu == '内存':
            plt.plot(times, memory, color='green', label=example_cpu)
        elif example_cpu == '磁盘':
            plt.plot(times, disk, color='orange', label=example_cpu)
        ax.xaxis.set_major_locator(ticker.MaxNLocator(intervst))
        plt.gcf().subplots_adjust(bottom=0.2)  # 保证底部显示完全
        plt.xlabel("时间", fontsize=13)
        plt.ylabel(f"{example_cpu}使用率 (%)", fontsize=13)
        plt.legend(loc='upper right')
        plt.savefig(f"./{example_cpu}.png")
        plt.close()
    def statistics(self, i):
        intervst = self.interval(i)
        try:
            while True:
                cpu_usage = psutil.cpu_percent(interval=1)
                cpu.append(cpu_usage)
                memory_usage = psutil.virtual_memory().percent
                memory.append(memory_usage)
                disk_usage = psutil.disk_usage('/').percent
                disk.append(disk_usage)
                net = psutil.net_io_counters()
                current_time = datetime.datetime.now()
                times.append(current_time.strftime("%m-%d") + "\n" + current_time.strftime("%H:%M:%S"))
                print(current_time, "    ", str(cpu_usage) + "%    ", str(memory_usage) + "%    ",
                      str(disk_usage) + "%")
                # 隔多久采集一次
                time.sleep(0)
                e = time.time()
                if e - s > i:
                    break
        except Exception as e:
            print(e)
        finally:
            self.paint("cpu",intervst)
            self.paint("内存",intervst)
            self.paint("磁盘",intervst)


if __name__ == '__main__':
    i = input("输入监控时长(秒)\n")
    Monitor().statistics(int(i))
