from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lmax=[0]*len(nums)
        rmin=[0]*len(nums)
        
        lmax[0]=nums[0]
        rmin[-1]=nums[-1]
        
        for i in range(1,len(nums)):
            lmax[i]=max(nums[i],lmax[i-1])
            
            # rmin[len(nums)-i-1]=min(nums[len(nums)-i-1],rmin[len(nums)-i])
            
        for i in range(len(nums)-2,-1,-1):
            rmin[i]=min(nums[i],rmin[i+1])
            
        for i in range(1,len(nums)):
            if lmax[i-1]<=rmin[i]:
                return i
        return len(nums)
    
sol=Solution()
nums = [5,0,3,8,6]
# nums = [1,1,1,0,6,12]
print(sol.partitionDisjoint(nums))
        