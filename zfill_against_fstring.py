import time
import random
inputs = [random.randint(1500000,2000000) for x in range(1,10000*1000) ]



out=[]
t1=time.time()
for i in inputs:
    out.append(format(i,'#025b'))
t2=time.time()
print(out[0])
print("first benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append('0b'+f'{i:b}'.zfill(25))
t2=time.time()
print(out[0])
print("second benchmark time: "+str(t2-t1))