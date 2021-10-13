

from typing import List


n=int(input())
p=int(input())
arr=[]
while n:
    n-=1
    arr.append(int(input()))
def fun(arr:List[int],n,p):
    arr.sort()
    days=arr[0]*p
    while days>0:
        sum_=sum([days//i for i in arr])
        if sum_==p:
            return days
        elif sum_<p:
            return days+1
        elif sum_>p:
            days-=1
print(fun(arr,n,p))
 
    