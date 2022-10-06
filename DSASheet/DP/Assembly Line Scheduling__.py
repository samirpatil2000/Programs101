class Solution:
    
    def carAssembly(self, a, t, e, x):
        dp = [[0] * len(a[0]) for _ in range(2)]
        dp[0][0] = a[0][0] + e[0]
        dp[1][0] = a[1][0] + e[1]
        
        for i in range(1, len(dp[0])):
            dp[0][i] = min(dp[0][i - 1] + a[0][i], 
                           dp[1][i - 1] + a[0][i] + t[1][i])
            dp[1][i] = min(dp[1][i - 1] + a[1][i], 
                           dp[0][i - 1] + a[1][i] + t[0][i])
        return min(dp[0][-1] + x[0], dp[1][-1] + x[1])
    
sol = Solution()
a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
  
print(sol.carAssembly(a, t, e, x))
            