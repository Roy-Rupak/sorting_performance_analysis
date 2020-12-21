import time
import numpy
import sys
def heapify(arr, i,n):
    r = 2*i+2
    l = 2*i+1
    largest = i
    if l < n and  arr[l]>arr[i] :
        largest = l
    if r < n and arr[r]>arr[largest] :
        largest = r
    if largest > i:
        temp=arr[i]
        arr[i]=arr[largest]
        arr[largest]=temp
        heapify(arr, largest,n)


def heapSort(arr):
    #Max heapify
    len_array=len(arr)-1
    array_half=len(arr)//2
    for i in range(array_half, -1, -1):
        heapify(arr, i,len(arr))
    #swap the root with the last element and call heapify
    for i in range(len_array, 0, -1):
        temp=arr[i]
        arr[i]=arr[0]
        arr[0]=temp
        heapify(arr, 0,i)

arr=[]
with open(sys.argv[1]) as f:
    content = f.read().splitlines()
for x in content:
    arr.append([int(x) for x in x.split()])
#print(arr)
time_list=[]
with open('output.txt', 'a') as the_file:
    for y in arr:
        n = len(y)
        ticks1 = time.time()
        heapSort(y)
        ticks2 = time.time()
        time_t=ticks2-ticks1
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
print("Standard deviation for various input size")
f=0
for x in range(len(time_list)//20):
    print(numpy.std(time_list[f:f+20]))
    f = f + 20
print("Average time for various input size")
print(avg)


