import time
import numpy
import sys
def partition(arr,low,high):
   i = low-1
   pivot = arr[high]
   for j in range(low , high):
      if arr[j] <= pivot:
         i+=1
         temp=arr[i]
         arr[i]=arr[j]
         arr[j]=temp
   temp = arr[i+1]
   arr[i+1] = arr[high]
   arr[high] = temp
   k=i+1
   return k
def quickSort(arr,low,high):
   if low < high:
      index = partition(arr,low,high)
      quickSort(arr, low, index-1)
      quickSort(arr, index+1, high)
arr=[]
time_list=[]
with open(sys.argv[1]) as f:
    content = f.read().splitlines()
for x in content:
    arr.append([int(x) for x in x.split()])
#print(arr)
with open('output.txt', 'a') as the_file:
    for y in arr:
        n = len(y)
        ticks1 = time.time()
        quickSort(y, 0, n - 1)
        ticks2 = time.time()
        time_t = ticks2 - ticks1
        time_list.append(time_t)
        the_file.write(' '.join(str(e) for e in y))
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
