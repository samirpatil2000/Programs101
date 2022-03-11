

from tracemalloc import start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        curr_idx = 0
        while i < len(nums):
            start_idx = i
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            len_ = i - start_idx + 1
            freq_ = min(len_, 2)
            while freq_ > 0:
                freq_ -= 1
                nums[curr_idx] = nums[start_idx]
                curr_idx += 1
            i += 1
        return curr_idx
    
    
sol = Solution()
nums = [1,1,2,2,3,4,4]
nums = [0,0,1,1,1,1,2,3,3]
print(sol.removeDuplicates(nums))
            
        