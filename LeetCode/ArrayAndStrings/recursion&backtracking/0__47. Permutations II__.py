
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def dfs(nums: List[int],out=[]):
            if len(nums)==0:
                result.append(out)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[0:i]+nums[i+1:],out+[nums[i]])
                
        dfs(nums)
        return result
    
    # def dfs(self, nums, path, res):
    #     if not nums:
    #         res.append(path)
    #     for i in range(len(nums)):
    #         if i > 0 and nums[i] == nums[i-1]:
    #                 continue
    #         self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
sol=Solution()
print(sol.permuteUnique([1,3,1]))
            
            