import math
import random
import threading
arrival_times=[]
next_time=0
next_ser_time=0
rateParameter=10
service_times=[]
serviceRate=15
i=0
n=0
def arrive():
    global n
    n=n+1
    print('{0} Arrived'.format(n))
    if(n==1):
        start_ser()
for i in range(30):
    time= -math.log(1.0 - random.random()) / rateParameter
    next_time=next_time+time
    arrival_times.append(next_time)
def dep():
    global n
    print('{0} departed'.format(0))

for i in range(30):
    time_s= -math.log(1.0 - random.random()) / serviceRate
    next_ser_time=next_ser_time+time
    service_times.append(next_time)
print(arrival_times)
print(service_times)
timer1=threading.Timer(arrival_times[i],arrive)
timer1.start()
timer2=threading.Timer(arrival_times[1],arrive)
timer2.start()
timer3=threading.Timer(arrival_times[28],arrive)
timer3.start()
def start_ser():
    t1=threading.Timer(service_times[0],dep)
    t1.start()
    t2=threading.Timer(service_times[1],dep)
    t2.start()
    t3=threading.Timer(service_times[3],dep)


