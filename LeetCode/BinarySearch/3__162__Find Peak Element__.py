from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return l

sol=Solution()
nums = [1,2,1,3,5,6,4]
nums = [2,3]
print(sol.findPeakElement(nums))