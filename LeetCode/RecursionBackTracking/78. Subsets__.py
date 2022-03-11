from typing import List
from unittest import result


class Solution:
    def subsets(self, nums: List[int], ) -> List[List[int]]:
        result = []
        def dfs(nums, list_so_far=[]):
            if len(nums) == 0:
                result.append(list_so_far)
                return
            dfs(nums[1:], list_so_far + []) 
            dfs(nums[1:], list_so_far + [nums[0]]) 
        dfs(nums)
        return result
            
        
            
            
        # result = self.subsets(nums, index + 1)
        # for i in range(len(result)):
        #     result[i] += [nums[index]]
        # return result + [[]]
        
    
        

sol = Solution()
nums = [0]
print(sol.subsets(nums))