import math
import random
import threading
arrival_times=[]
next_time=0
rateParameter=10
def arrive:
    print('Arrived')
for i in range(30):
    time= -math.log(1.0 - random.random()) / rateParameter
    next_time=next_time+time
    arrival_times.append(next_time)
print(arrival_times)
time1=threading.Timer(arrival_times[i],arrive)
time1=threading.Timer(arrival_times[i+1],arrive)
time1=threading.Timer(arrival_times[i+2],arrive)
time1=threading.Timer(arrival_times[i+3],arrive)
time1=threading.Timer(arrival_times[i+4],arrive)
time1=threading.Timer(arrival_times[i+5],arrive)
time1=threading.Timer(arrival_times[i+6],arrive)
time1=threading.Timer(arrival_times[i+7],arrive)
time1=threading.Timer(arrival_times[i+8],arrive)
time1=threading.Timer(arrival_times[i+9],arrive)
time1=threading.Timer(arrival_times[i+10],arrive)
time1=threading.Timer(arrival_times[i+11],arrive)
time1=threading.Timer(arrival_times[i+12],arrive)
time1=threading.Timer(arrival_times[i+13],arrive)
time1=threading.Timer(arrival_times[i+14],arrive)


