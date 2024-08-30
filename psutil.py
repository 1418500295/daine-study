import psutil
import time
import datetime

cpu = []
memory = []
io = []
times = []
print("当前日期     时间          CPU使用率 内存使用率 磁盘使用率")
s = time.time()
while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu.append(cpu_usage)
    memory_usage = psutil.virtual_memory().percent
    memory.append(memory_usage)
    disk_usage = psutil.disk_usage('/').percent
    io.append(disk_usage)
    net = psutil.net_io_counters()
    current_time = datetime.datetime.now()
    times.append(current_time.strftime("%m-%d")+"\n"+current_time.strftime("%H:%M:%S"))
    print(current_time,"    ",str(cpu_usage)+"%    ",str(memory_usage)+"%    ",str(disk_usage)+"%")
    # 隔多久采集一次
    time.sleep(0)
    e = time.time()
    if e - s > 20:
        break
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
x = times
y1 = cpu
y2 = memory
y3 = io
plt.figure(figsize=(10,7))
plt.xticks(rotation=45,fontsize=8)
plt.plot(x,y1,'o-',color='red',label='cpu')
plt.xlabel("时间")
plt.ylabel("cpu使用率")
# for a, b in zip(x, y1):
#     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据
plt.savefig("./cpu.png")
plt.close()
# plt.show()

plt.figure(figsize=(10,7))
plt.xticks(rotation=45,fontsize=8)
plt.plot(x,y2,'o-',color='green',label='memory')
plt.xlabel("时间")
plt.ylabel("内存使用率")
# for a, b in zip(x, y2):
#     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据

plt.savefig("./内存.png")
plt.close()


plt.figure(figsize=(10,7))
plt.xticks(rotation=45,fontsize=8)
plt.plot(x,y3,'o-',color='blue',label='磁盘')
plt.xlabel("时间")
plt.ylabel("磁盘使用率")
# for a, b in zip(x, y3):
#     plt.text(a, b+0.1,b, ha='center', va='bottom', fontsize=8)#y_axis_data1加标签数据

plt.savefig("./磁盘.png")
plt.close()








