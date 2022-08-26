class Solution:
    
    def matrix_multiplication(self, arr):
        dp = [[0]*(len(arr) - 1) for _ in range(len(arr) - 1)]
        for gap in range(len(dp)):
            for row, col in enumerate(range(gap, len(dp))):
                if gap == 0:
                    dp[row][col] = 0
                elif gap == 1:
                    dp[row][col] = arr[row] * arr[col] * arr[col + 1]
                else:
                    result = 2 ** 32
                    for k in range(row, col):
                        left = dp[row][k]
                        right = dp[k + 1][col]
                        multi = arr[row] * arr[k + 1] * arr[col + 1]
                        result = min(left + right + multi, result)
                    dp[row][col] = result
        return dp[0][-1]
    
arr = [40, 20, 30, 10, 30]
print(Solution().matrix_multiplication(arr))
                         
                        
                
                
            
            