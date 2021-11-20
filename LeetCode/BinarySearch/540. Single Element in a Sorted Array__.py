from typing import List


class Solution:
    def isFirst(self,nums:List[int],index:int):
        if index+1<len(nums):
            if nums[index]==nums[index+1]:
                return True
        return False
        
        
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if mid-1>0 and mid<len(nums)-1:
                if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1] :
                    return nums[mid]
            if mid&1!=1: #even
                if self.isFirst(nums,mid):
                    left=mid+1
                else:
                    right=mid-1
            else:
                if self.isFirst(nums,mid):
                    right=mid-1
                else:
                    left=mid+1
        return nums[left]
    
sol=Solution()
nums = [1,1,2,3,3,4,4,8,8]
nums = [3,3,7,7,11]
print(sol.singleNonDuplicate(nums))