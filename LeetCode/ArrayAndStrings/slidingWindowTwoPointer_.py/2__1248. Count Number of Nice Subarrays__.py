from typing import List


class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
        i=0
        j=0
        count_=0
        while j<len(arr) and i<len(arr):
            while j<len(arr) and k>0:
                if arr[j]%2!=0:
                    k-=1
                j+=1
            if k==0:
                count_+=1
            while i<len(arr):
                if arr[i]%2!=0:
                    k+=1
                if k==0:
                    count_+=1
                i+=1
        return count_
            
sol=Solution()
nums = [1,1,2,1,1]
k = 3
nums = [2,4,6]
k = 1
nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(sol.numberOfSubarrays(nums,k))