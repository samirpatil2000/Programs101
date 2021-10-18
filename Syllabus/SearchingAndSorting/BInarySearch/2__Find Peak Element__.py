from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while right-left>0:
            mid=(left+right)//2
            right_=nums[mid+1] if mid+1<len(nums) else -2**32
            if nums[mid]>right_:
                right=mid
            else:
                left=mid+1
        return nums[left]
    
        


nums=[1,2,3,1]
nums=[-1,0,2]
sol=Solution()
print(sol.findPeakElement(nums))