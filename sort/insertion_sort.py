import time
import numpy
import sys
def insertion_sort(insertion_list):
   n=len(insertion_list)
   for x in range(1,n):
       prev = insertion_list[x]
       while x!=0 and prev<insertion_list[x-1]:
            insertion_list[x] = insertion_list[x-1]
            x -=1
       insertion_list[x] = prev
   return insertion_list



i=0
lines1=[]
lines2=[]
time_list=[]
with open(sys.argv[1]) as f:
    content = f.read().splitlines()
for x in content:
    lines2.append([int(x) for x in x.split()])
#print(lines2)
for y in lines2:
    ticks1 = time.time()
    insertion_sort(y)
    ticks2 = time.time()
    time_t = ticks2 - ticks1
    time_list.append(time_t)
with open('output.txt', 'a') as the_file:
    for y in lines2:
        the_file.write(' '.join(str(e) for e in insertion_sort(y)))
        the_file.write('\n')
sum_=0
avg=[]
for x in range(len(time_list)):
    if (x+1) % 20 == 0:
        avg.append(sum_*1.0/20)
        sum_=0
    sum_ += time_list[x]
#print(time_list)
f=0
print("Standard deviation for various input size")
for x in range(len(time_list)//20):
    print(numpy.std(time_list[f:f+20]))
    f = f + 20
print("Average time for various input size")
print(avg)
