from typing import List


class Solution:
    def searchRight(self,nums:List[int],left:int,right:int,target:int):
        if left>right:return -1
        mid=(left+right)//2
        
        if nums[mid]==target and mid==len(nums)-1:
            return mid
        if nums[mid]==target and nums[mid+1]!=target:
            return mid
        else:
            if nums[mid]<=target:
                return self.searchRight(nums,mid+1,right,target)
            else:
                return self.searchRight(nums,left,mid-1,target)
    
    def searchLeft(self,nums:List[int],left:int,right:int,target:int):
        if left>right:return -1
        mid=(left+right)//2
        if nums[mid]==target and mid==0:
            return mid
        if nums[mid]==target and nums[mid-1]!=target:
            return mid
        else:
            if nums[mid]>=target:
                return self.searchLeft(nums,left,mid-1,target)
            else:
                return self.searchLeft(nums,mid+1,right,target)
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if n==0:
            return [-1,-1]
        n-=1
        return [self.searchLeft(nums,0,n,target),self.searchRight(nums,0,n,target)]

sol=Solution()
nums = []
target = 6
print(sol.searchRange(nums,target))
        