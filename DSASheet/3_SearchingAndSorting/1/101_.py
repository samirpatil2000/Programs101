#code
def findFirstOccurence(arr,left,right,val):
    mid=(left+right)/2
    if(arr[mid]==val and arr[mid]!=arr[mid-1]):
        return mid
    elif(arr[mid]==val and arr[mid]==arr[mid-1]):
        return findFirstOccurence(arr,left,mid,val)
    else:
        if(arr[mid]>val):
            return findFirstOccurence(arr,left,mid,val)
        else:
            return findFirstOccurence(arr,mid,right,val)
    
    if(left>=right):
        return -1
        
def findLastOccurence(arr,left,right,val):
    mid=(left+right)/2
    if(arr[mid]==val and arr[mid]!=arr[mid+1]):
        return mid
    elif(arr[mid]==val and arr[mid]==arr[mid+1]):
        return findLastOccurence(arr,mid,right,val)
    else:
        if(arr[mid]>val):
            return findLastOccurence(arr,left,mid,val)
        else:
            return findLastOccurence(arr,mid,right,val)
    if(left>=right):
        return -1

t=int(input())
while(t>0):
    t=t-1
    n=int(input())
    m=int(input())
    list=[i for i in range(0,n)]
    for i in range(0,n):
        list[i]=int(input())
    # list=eval(input())
    print(findFirstOccurence(list,0,n,m),findLastOccurence(list,0,n,m))
    
import sys
    
    
    
def get_arr(): return list(map(int, sys.stdin.readline().strip().split()))
Arr = get_arr()

def get_ints(): return map(int, sys.stdin.readline().strip().split())
a,b,c,d = get_ints()