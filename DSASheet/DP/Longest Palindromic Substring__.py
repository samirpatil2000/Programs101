class Solution:
    
    def longestPalindrome(self, S):
        dp = [[None]* len(S) for _ in range(len(S))]
        result = ""
        for gap in range(len(S)):
            row = 0
            col = gap
            while col < len(S):
                if gap == 0:
                    dp[row][col] = S[row]
                elif gap == 1:
                    if S[row] == S[col]:
                        dp[row][col] = S[row] + S[col]
                else:
                    if S[row] == S[col] and dp[row + 1][col - 1] != None:
                        dp[row][col] = S[row] + dp[row + 1][col - 1] + S[col]
                if dp[row][col] and len(dp[row][col]) > len(result):
                    result = dp[row][col]
                row += 1
                col += 1
        return result
sol = Solution()
S = "aaaabbaa"
print(sol.longestPalindrome(S))
