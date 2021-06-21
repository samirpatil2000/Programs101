from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums)==2:return max(nums)
        def dfs(n,m,dp={}):
            
            if n in dp:return dp[n]
            if n>m:return 0
            # print(n)
            x=max(dfs(n+2,m,dp)+nums[n],dfs(n+1,m,dp))
            dp[n]=x
            return x
        return max(dfs(n=1,m=len(nums)-1),dfs(n=0,m=len(nums)-2))
    
    def robTabulation(self, nums: List[int]) -> int: 
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums)
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(dp)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
                    
sol=Solution()
nums=[2,3,2]

print(sol.rob(nums))
print(sol.robTabulation(nums))
            
            
            