import sys
def missingNumber(arr,n):
    i=0
    while i <len(arr):
        
        if arr[i]<len(arr) and arr[i]!=i+1:
            temp=arr[i]
            arr[i]=arr[temp-1]
            arr[temp-1]=temp
        else:
            i+=1
    for i in range(len(arr)):
        if i!=arr[i]-1:
            return i+1
    return n

n=int(input())
arr=list(map(int,sys.stdin.readline().strip().split()))
# arr=[1,2,4,3]
# arr=[2 ,3, 1, 5]
# # arr=[1,2,4,6,3,7,8]
# n=2
# arr=[1]
print(missingNumber(arr,n))