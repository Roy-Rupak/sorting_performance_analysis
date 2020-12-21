import time
import numpy
import sys
def mergeSort(merge_list):
    if len(merge_list)>1:
       i, j, k = 0, 0, 0
       mid = len(merge_list)//2
       left= merge_list[:mid]
       right = merge_list[mid:]
       l_len = len(left)
       r_len = len(right)
       mergeSort(left)
       mergeSort(right)

       while  j < r_len and i < l_len :
           if left[i] < right[j]:
               merge_list[k] = left[i]
               i += 1

           else:
               merge_list[k] = right[j]
               j += 1

           k+=1

       while i < l_len:
           merge_list[k]=(left[i])
           i+=1
           k+=1

       while j < r_len:
           merge_list[k]=(right[j])
           j+=1
           k+=1
    return merge_list



i=0
lines1=[]
lines2=[]
with open(sys.argv[1]) as f:
    content = f.read().splitlines()
for x in content:
    lines2.append([int(x) for x in x.split()])
#print(lines2)
time_list=[]
for y in lines2:
    ticks1 = time.time()
    mergeSort(y)
    ticks2 = time.time()
    time_t = ticks2 - ticks1
    time_list.append(time_t)
with open('output.txt', 'a') as the_file:
    for y in lines2:
        the_file.write(' '.join(str(e) for e in mergeSort(y)))
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
