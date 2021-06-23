from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        # if len(nums)==1:
        #     return []
        def rec(arr,list_=[]):
            if len(arr)==0:
                result.append(list_)
                return  
            for i in range(len(arr)):
                rec(arr[:i]+arr[i+1:],list_+[arr[i]])
        rec(nums)
        return result
sol=Solution()
nums=[1]
print(sol.permute(nums))