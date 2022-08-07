class Solution:
    def count(self, arr, m, target): 
        # code here
        dp = [0] * (target + 1)
        dp[0] = 1 
        for i in range(len(arr)):
            for j in range(arr[i], len(dp)):
                dp[j] += dp[j - arr[i]]
        print(dp)
        return dp[-1]
                            
    
sol = Solution()
arr = [1, 2, 3]
n = 4
print(sol.count(arr, len(arr), n))