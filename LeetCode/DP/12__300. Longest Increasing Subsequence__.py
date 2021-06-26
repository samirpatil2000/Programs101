from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(1,len(dp)):
            max_=0
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    max_=max(max_,dp[j])
            
            dp[i]=max_+1
        return max(dp)
    
    
sol=Solution()
nums=[1,3,6,7,9,4,10,5,6]
print(sol.lengthOfLIS(nums))