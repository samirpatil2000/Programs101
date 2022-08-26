class Solution:
    
    def nCr(self, n, r):
        if n < r:
            return 0
        r = min(n - r, r)
        mod = 10e8 + 7
        dp = [0]* (r + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, r), 0, -1):
                dp[j] = (dp[j] + dp[j - 1]) % mod
        return int(dp[-1])
    
n, r =778, 116
print(Solution().nCr(n, r))
                
                
                
                        
        