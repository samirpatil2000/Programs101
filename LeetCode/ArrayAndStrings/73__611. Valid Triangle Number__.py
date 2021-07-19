from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n<3:
            return 0
        nums.sort()
        count=0
        for i in range(2,n):
            left=0
            right=i-1
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    count+=(right-left)
                    right-=1
                else:
                    left+=1
                    
        return count
    
    
sol=Solution()
nums= [2,2,3,4]
nums=[4,2,3,4]
print((sol.triangleNumber(nums)))