import math
import random
import threading
arrival_times=[]
next_time=0
rateParameter=10
for i in range(30):
    time= -math.log(1.0 - random.random()) / rateParameter
    next_time=next_time+time
    arrival_times.append(next_time)
print(arrival_times)
