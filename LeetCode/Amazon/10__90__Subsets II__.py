from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        
        def dfs(nums,index=0,out_=[]):
            result.append(out_)
            for i in range(index,len(nums)):
                if i!=index and nums[i-1]==nums[i]:
                    continue
                dfs(nums,index+1,out_+[nums[i]])   
        dfs(nums)
        return result
        

sol=Solution()
nums=[0,2,3]
nums=[4,4,4,1,4]
print(sol.subsetsWithDup(nums))