class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wts, vals, n):
        
        dp = [[0] * (W + 1) for _ in range (n + 1)]
        result = 0
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                
                val = vals[row - 1]
                wt = wts[row - 1]
                dp[row][col] = dp[row - 1][col]
                if col >= val:
                    dp[row][col] = max(
                        dp[row - 1][col - val] + wt, dp[row - 1][col]
                    )
                    
                result = max(dp[row][col], result)
                
        print(dp)
        return result
    
sol = Solution()
W = 7
wts = [15, 14, 10, 45, 30]
vals = [2, 5, 1, 3, 4]

W = 4
vals = [1, 2, 3]

wts= [4, 5, 1]
print(sol.knapSack(W, wts, vals, len(wts)))



# n = 3

# x = [[0] * n] * n
# y = [[0] * n for _ in range(n)]

# print(x, type(x))
# print(y, type(y))
# print(x == y) 


# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0:
#             x[row][col] = -1
#             y[row][col] = -1

# print(x, type(x))
# print(y, type(y))
# print(x == y)


