import psutil
import time
import datetime

run_time = 900
cpu = []
memory = []
io = []
times = []
print("当前日期     时间          CPU使用率 内存使用率 磁盘使用率")
s = time.time()

def interval():
    interval = None
    if 0 <= run_time <= 300:
        interval = 11
    elif 300 < run_time <= 600:
        interval = 16
    elif 600 < run_time:
        interval = 21
    return interval
try:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu.append(cpu_usage)
        memory_usage = psutil.virtual_memory().percent
        memory.append(memory_usage)
        disk_usage = psutil.disk_usage('/').percent
        io.append(disk_usage)
        net = psutil.net_io_counters()
        current_time = datetime.datetime.now()
        times.append(current_time.strftime("%m-%d") + "\n" + current_time.strftime("%H:%M:%S"))
        print(current_time, "    ", str(cpu_usage) + "%    ", str(memory_usage) + "%    ", str(disk_usage) + "%")
        # 隔多久采集一次
        time.sleep(0)
        e = time.time()
        if e - s > run_time:
            break
except Exception as e:
    print(e)
finally:
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider
    import matplotlib.ticker as ticker

    x = times
    y1 = cpu
    y2 = memory
    y3 = io
    plt.rcParams['font.family'] = 'SimHei'
    fig = plt.figure(figsize=(20, 7))
    ax = fig.add_subplot(111)
    plt.xticks(rotation=45, fontsize=13)
    plt.yticks(fontsize=13)
    plt.plot(x, y1, color='red', label='cpu')
    ax.xaxis.set_major_locator(ticker.MaxNLocator(interval()))
    plt.gcf().subplots_adjust(bottom=0.2)  #保证底部显示完全
    plt.xlabel("时间",fontsize=13)
    plt.ylabel("cpu使用率 (%)",fontsize=13)
    plt.legend(loc='upper right')
    # plt.grid(linestyle='--')

    # for a, b in zip(x, y1):
    #     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据
    plt.savefig("./cpu.png")
    plt.close()
    # plt.show()



    fig = plt.figure(figsize=(20, 7))
    ax = fig.add_subplot(111)
    plt.xticks(rotation=45, fontsize=13)
    plt.yticks(fontsize=13)
    plt.plot(x, y2, color='green', label='内存')
    ax.xaxis.set_major_locator(ticker.MaxNLocator(interval()))
    plt.gcf().subplots_adjust(bottom=0.2) #保证底部显示完全
    plt.xlabel("时间",fontsize=13)
    plt.ylabel("内存使用率 (%)",fontsize=13)
    plt.legend(loc='upper right')
    # plt.grid(linestyle='--')


    # for a, b in zip(x, y2):
    #     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据

    plt.savefig("./内存.png")
    plt.close()


    fig = plt.figure(figsize=(20, 7))
    ax = fig.add_subplot(111)
    plt.xticks(rotation=45, fontsize=13)
    plt.yticks(fontsize=13)
    plt.plot(x, y3, color='blue', label='磁盘')
    ax.xaxis.set_major_locator(ticker.MaxNLocator(interval()))
    plt.gcf().subplots_adjust(bottom=0.2)  #保证底部显示完全
    plt.xlabel("时间",fontsize=13)
    plt.ylabel("磁盘使用率 (%)",fontsize=13)
    plt.legend(loc='upper right')
    # plt.grid(linestyle='--')



    # for a, b in zip(x, y3):
    #     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据

    plt.savefig("./磁盘.png")
    plt.close()










