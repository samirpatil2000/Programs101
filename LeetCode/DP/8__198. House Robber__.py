from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int: 
        
        def dfs(n,dp={}):
            
            if n in dp:return dp[n]
            if n>=len(nums):return 0
            # print(n)
            x=max(dfs(n+2,dp)+nums[n],dfs(n+1,dp))
            dp[n]=x
            return x
        return dfs(0)
    
    def robTabulation(self, nums: List[int]) -> int: 
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(dp)):
        
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]

    
    def robMemo(self, nums: List[int],memo={},index=0) -> int:
        if index in memo:return memo[index]
        if index>=len(nums):
            return 0
        max_=max( 
                    self.robMemo(nums,memo,index+2)+nums[index],
                    self.robMemo(nums,memo,index+1),
                )
        memo[index]=max_
        return max_
sol=Solution()
nums=[2,7,9,3,1]
nums=[1,3,1,3,100]

print(sol.rob(nums))
# print(sol.robTabulation(nums))
print(sol.robMemo(nums))
            
            
            