from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        i=0
        count_=0
        while i<len(nums):
            len_=0
            max_=nums[i]
            while i<len(nums) and max_>=left and max_<=right:
                print(nums[i],max_)
                max_=max(max_,nums[i])
                len_+=1
                i+=1
                # count_+=
                
            # print(len_)
            # count_+=(len_*(len_+1)//2)
            i+=1
        return count_
    
sol=Solution()
nums = [2, 1, 4, 3]
left = 2
right = 3
print(sol.numSubarrayBoundedMax(nums,left,right))
            