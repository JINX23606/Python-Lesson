#var
n = 0
#print('n =',n)

n = 'abc'
#print('n = ',n)
n,m = 0,'abc'
n,m,z = 0.125,'abc',False

n = n+1 #good
n += 1 #good
# n++ #bad 
n=4
n = None
#print('n =',n)

#if
n = 2
if n>2:
    n-=1
elif n==2:
    n*= 2
else:
    n+=2
#print(n)

n,m = 4,5
if ((n>2 and
     n!= m) or n==m):
    n+=1
#print(n)

#loop
n = 5
while n < 5:
    print(n)
    n+=1
    for i in range(5):
        print(i)
    for i in range(2,6):
        print(i)
    for i in range(5,1,-1):
        print(i)

#math
import math
print(math.fmod(-10,3))

math.floor(3/2)
math.ceil(3/2)
math.sqrt(2)
math.pow(2,3)

float('inf')
float('-inf')

print(math.pow(2,200))
#bolean
print(math.pow(2,200)<float('inf'))

#Array / List
arr = [1,2,3]
print(arr)

arr.append(4)
arr.append(5)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

n=5
arr = [1]*n
print(arr)
print(len(arr))

arr = [1,2,3]
print(arr[-3]) #-3-2-1
print(arr[-2])
arr = [1,2,3,4]
print(arr[1:3]) #value -1
print(arr[0:4])
print(arr[0:10])#all
a,b,c = [1,2,3]
print(a,b,c)
# loop through array
nums = [1,2,3]
#Using index
for i in range(len(nums)):
    print(nums[i])
#without index
for n in nums:
    print(n)
#with index and value 
for i,n in enumerate(nums):
    print(i,n)
# Loop through multiple arrays simultaneously with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(i,n)
#Reverse
nums = [1,2,3]
nums.reverse()
print(nums)

#Sorting
arr = [5,4,3,2,1]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

#sort a-z
arr = ['bob','alice','jane','doe']
arr.sort()
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x:len(x))
print(arr)

#List comprehensive
arr = [i for i in range (5)]
print(arr)

#2D lists
arr = [[0]*4 for i in range(4)]
print(arr)
print(arr[0][0],arr[3][3])

#list combo
arr = ['bob','alice','jane','doe']
for i in range(len(arr)):
    print(str(i+1)+'.'+arr[i])

#string
s = 'abc'
print(s[0:2])
s += 'def'
print(s)
#int
print(int('123')+int('123'))
#str
print(str(123) + str(123))
#curious
print(ord('a'))
print(ord('b'))

#List to String
String = ['A','B','C']
print(''.join(String))
#String to list
String = 'ABC'
print(String.split(' ,'))

#Queue -> List
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

#HashSet ->
mySet= set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
#Boolean
print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)
#list to set
print(set([1,2,3]))

mySet = {i for i in range(5)}
print(mySet)

#Hashmap aka Dict
myMap = {}
myMap['Alice']=88
myMap['bob']=77
print(myMap)
print(len(myMap))

myMap['Alice']=80
print(myMap)

print('Alice' in myMap)
myMap.pop('Alice') #remove
print('Alice' in myMap)

myMap = {
    'Alice':88,
    'bob':77
}
print(myMap)
#Comprehension
myMap = {i:2*i for i in range(3)}
print(myMap)

myMap = {
    'Alice':90,
    'Bob':80
}
for key in myMap:
    print(key,myMap[key])

for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key,val)

#Tuples
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

myMap = {(1,2):3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2)in mySet)

#Heaps
import heapq

minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

maxHeap = []
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-4)

print(-1*maxHeap[0])

while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))

arr = [2,1,8,4,5]
heapq.heapify(arr) #sort
while arr:
    print(heapq.heappop(arr))

#Functions
def myfunc(n,m):
    return n*m
print(myfunc(3,4))

def outer(a,b):
    c = 'c'
    def inner():
        return a+b+c
    return inner()

print(outer('a','b'))

def double(arr,val):
    def helper():

        for i,n in enumerate(arr):
            arr[i] *= 2
        
        nonlocal val
        val *= 2
    helper()
    print(arr,val)

nums =[1,2]
val = 3
double(nums,val)

#Classes
class myclass:
    def __init__(self,nums):
        self.nums = nums
        self.size = len(nums)
    def get_length(self):
        return self.size
    def double_lenght(self):
        return 2*self.get_length()
my_obj = myclass([1,2,3])
print(my_obj.get_length())
print(my_obj.double_lenght())
    