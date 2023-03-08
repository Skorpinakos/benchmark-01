
import time
import random
inputs = [random.randint(1500000,2000000) for x in range(1,10000*1000) ]



out=[]
t1=time.time()
for i in inputs:
    out.append(bin(i)[2:].zfill(25))
t2=time.time()
print(out[0])
print("first benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append(format(i,'b').zfill(25))
t2=time.time()
print(out[0])
print("second benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append(bin(i).lstrip('-0b').zfill(25))
t2=time.time()
print(out[0])
print("third benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append(f'{i:b}'.zfill(25))
t2=time.time()
print(out[0])
print("fourth benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append(bin(i).replace("0b","").zfill(25))
t2=time.time()
print(out[0])
print("fifth benchmark time: "+str(t2-t1))

out=[]
t1=time.time()
for i in inputs:
    out.append('{:025b}'.format(i))
t2=time.time()
print(out[0])
print("sixth benchmark time: "+str(t2-t1))
