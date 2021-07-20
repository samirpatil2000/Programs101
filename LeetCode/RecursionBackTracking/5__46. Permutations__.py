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
    def anotherMethod(self,nums):
        res=[]
        
        def dfs(index,arr):
            if index == len(arr):
                res.append(arr)
                return
            for i in range(index,len(nums)):
                arr[index],arr[i]=arr[i],arr[index]
                print(index,arr)
                dfs(index+1,arr)
                
                arr[index],arr[i]=arr[i],arr[index]
                print(index,arr)
        dfs(0,nums)
        
        return res
sol=Solution()
nums=[1,2]
# nums=[1]
print(sol.permute(nums))
print(sol.anotherMethod(nums))