from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # def coin_change(amount,memo={}):
        #     if amount==0:return 0
        #     if amount<0:return 2**32
        #     if amount in memo:return memo[amount]
        #     memo[amount]=min([coin_change(amount-c,memo) for c in coins])+1
        #     return memo[amount]
        # result=coin_change(amount)
        # return -1 if result>=2**32 else result
        big=float('inf')
        dp=[0]+[big]*(amount)
        for col in range(amount+1):
            for c in coins:
                if col-c>=0:dp[col]=min(dp[col-c]+1,dp[col])
        return -1 if dp[-1] == float('inf') else dp[-1]
    
sol=Solution()
coins = [1,2,5]
amount = 11
# coins = [2]
# amount = 11
# coins = [1]
# amount = 0
print(sol.coinChange(coins,amount))