from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # left=0
        # right=len(nums)-1
        # ans=0
        # while left<right:
        #     mid=left+(right-left)//2
        #     if nums[mid]==target:return mid
        #     if nums[mid]<target:
        #         ans=mid
        #         left=mid+1
        #     else:
        #         ans=-1
        #         right=mid
        # if nums[left]==target:return left
        # if nums[left]<target:return left+1
        # return ans+1
        
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
    
    
sol=Solution()
nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
# target = 2
# target = 0
target=7
print(sol.searchInsert(nums,target))