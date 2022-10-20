class Solution:
    
    def get_coins_count(self, target, coins, dp = {}):
        if target in dp:
            return dp[target]
        if target == 0:
            return True, 0
        if target < 0:
            return False, -1
        min_ = 2 ** 32
        ans = False
        for coin in coins:
            result = self.get_coins_count(target - coin, coins, dp)
            if result[0]:
                min_ = min(min_, result[1])
                ans = True
        dp[target] = (ans, min_ + 1)
        return dp[target]

target = 3
coins = [3, 5]
target, coins = 300, [1,2,3,4,3]
print(Solution().get_coins_count(target, coins)[1])