from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp=[[1]*len(nums) for _ in range(len(nums))]
        for g in range(len(nums)):
            row=0
            for col in range(g,len(nums)):
                max_=-1
                for k in range(row,col+1):
                    left= 0 if k==row else dp[row][k-1]
                    right= 0 if k==col else dp[k+1][col]
                    value=(1 if row==0 else nums[row-1])*nums[k]*(1 if col==len(nums)-1 else nums[col+1])
                    max_=max(max_,value+left+right)
                
                dp[row][col]=max_
                row+=1
        return dp[0][-1]
sol=Solution()
nums=(3,1,5,8)
print(sol.maxCoins(nums))
