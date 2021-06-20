from typing import List


"""Understand the concept behind this"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        start=0
        end=0
        windowSize=0
        count_=0
        while end<len(nums):
            if nums[end]>=left and nums[end]<=right:
                windowSize=end-start+1
            elif nums[end]>right:
                start=end+1
                windowSize=0
            
            elif nums[end]<left:
                windowSize=windowSize
            end+=1
            count_+=windowSize
            
        return count_
    
    
sol=Solution()
nums = [2, 1, 4, 3]
left = 2
right = 3
print(sol.numSubarrayBoundedMax(nums,left,right))