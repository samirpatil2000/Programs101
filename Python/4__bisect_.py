import bisect

arr=[1,2,6,7,8,12,34,56,78]
print(bisect.bisect(arr,1))
bisect.insort(arr,0)
bisect.insort(arr,13)
print(arr)