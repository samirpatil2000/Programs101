from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums)==2:return max(nums)
        def dfs(n,m,dp):
            if n in dp:return dp[n]
            if n>m:return 0
            # print(n)
            x=max(dfs(n+2,m,dp)+nums[n],dfs(n+1,m,dp))
            dp[n]=x
            return x
        return max(dfs(n=1,m=len(nums)-1,dp={}),dfs(n=0,m=len(nums)-2,dp={}))
    
    def robTabulation(self, nums: List[int]) -> int: 
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums)
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(dp)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
    
    def robMemo(self,nums:List[int]):
        def dfs(index:int,first:bool,memo={}):
            if index in memo:return memo[index]
            if index>=len(nums):
                return 0
            if index==len(nums)-1 and first:
                return 0
            max_=max(dfs(index+2,first,memo)+nums[index],
                       dfs(index+1,first,memo))
            memo[index]=max_
            return max_
        return max(dfs(2,True)+nums[0],dfs(1,False))
                    
sol=Solution()
nums=[2,3,2]
nums=[94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]
print(sol.rob(nums))
print(sol.robTabulation(nums))
print(sol.robMemo(nums))
            
            
            