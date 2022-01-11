from typing import List


class Solution:
    def minMulti(self, nums: List[int]) -> int:
        n=len(nums)-1
        dp=[[0]*n for _ in range(n)]
        for gap in range(n):
            for row,col in enumerate(range(gap,n)):
                if gap==0:
                    dp[row][col]=0
                elif gap==2:
                    dp[row][col]=nums[row]*nums[col]*nums[col+1]
                else:
                    min_=2**32
                    for k in range(row,col):
                        left_cost=dp[row][k]
                        right_cost=dp[k+1][col]
                        multi_cost=nums[row]*nums[k+1]*nums[col+1]
                        total=left_cost+right_cost+multi_cost
                        min_=min(total,min_)
                    dp[row][col]=min_
        return dp[0][-1]                
        
        
sol=Solution()
print(sol.minMulti(nums=(3,1,5,8)))