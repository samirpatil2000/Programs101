import sys
from typing import List
def fun(arr):
    i=0
    j=len(arr)-1
    while i<=j:
        if arr[i]%2==0 and arr[j]%2!=0:    
            i+=1
            j-=1
        elif arr[i]%2!=0 and arr[j]%2==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        else:
            if arr[i]%2==0:
                i+=1
            elif arr[j]%2!=0:
                j-=1

def get_ints():return list(map(int, sys.stdin.readline().strip().split()))

# n=int(input())
# arr=get_ints()
# # arr=[3,4]

# fun(arr)
# print(arr)
            
            
            
def fun(s):
    set_=set(list(['a','e','i','o','u','A','E','I','O','U']))
    return "".join([i for i in s if i not in set_])

# s=input()
# print(fun(s))


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_=[]
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        while i<len(nums1)and j<len(nums2):
            print(nums1[i],nums2[j])
            if nums1[i]==nums2[j]:
                list_.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
        return list_
            
            
sol=Solution()
nums1=[1,2,2,1]
nums2=[2,2]
print(sol.intersect(nums1,nums2))
        