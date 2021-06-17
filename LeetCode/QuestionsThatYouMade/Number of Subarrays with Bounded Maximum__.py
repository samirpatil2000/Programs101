from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        i=0
        count_=0
        while i<len(nums):
            len_=0
            while i<len(nums) and nums[i]>=left and nums[i]<=right:
                print(nums[i])
                len_+=1
                i+=1
            # print(len_,nums[:i])
            count_+=(len_*(len_+1)//2)
            i+=1

        return count_
    
sol=Solution()
nums = [2, 3,3, 4, 3]
left = 2
right = 3
print(sol.numSubarrayBoundedMax(nums,left,right))
            