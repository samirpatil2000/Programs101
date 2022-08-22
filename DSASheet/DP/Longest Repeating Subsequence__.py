class Solution:
    def LongestCommonSubsequence(self,x,y,s1,s2):
        
        # code here
        x += 1
        y += 1
        dp = [[0] * x for _ in range(y)]
        for row in range(y):
            for col in range(x):
                if row == 0 or col == 0:
                    continue
                if s2[row - 1] == s1[col - 1] and row != col:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]
    def LongestRepeatingSubsequence(self, str):
        return self.LongestCommonSubsequence(len(str), len(str), str, str)

str1 = "axxzxy"
str1 = "axxxy"
    
print(Solution().LongestRepeatingSubsequence(str1))
     