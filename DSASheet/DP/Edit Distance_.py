class Solution:
    	def editDistance(self, s, t):
		# Code here
            dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
            for row in range(len(t) + 1):
                for col in range(len(s) + 1):
                    if row == 0 and col == 0:
                        dp[row][col] = 0
                    elif row == 0:
                        dp[row][col] = dp[row][col - 1] + 1
                    elif col == 0:
                        dp[row][col] = dp[row - 1][col] + 1
                    else:
                        if t[row - 1] == s[col - 1]:
                            dp[row][col] = dp[row - 1][col - 1]
                        else:
                            dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
            return dp[-1][-1]

sol = Solution()
s = "geek"
t = "gesek"
# s = "gfg"
# t = "gfg"
s = "ecfbefdcfca" 
t = "badfcbebbf"
print(sol.editDistance(s, t))