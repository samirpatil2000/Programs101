class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def LongestCommonSubsequence(self,x,y,s1,s2):
        
        # code here
        x += 1
        y += 1
        dp = [[0] * x for _ in range(y)]
        for row in range(y):
            for col in range(x):
                if row == 0 or col == 0:
                    continue
                if s2[row - 1] == s1[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]
    
    
    
sol = Solution()
A = 6
B = 6
str1 = "ABCDGH"
str2 = "AEDFHR"
print(sol.LongestCommonSubsequence(A, B, str1, str2))