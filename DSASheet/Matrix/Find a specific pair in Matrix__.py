from typing import List


class Solution:
    
    def findMaxValuePair(self, mat:List[List[int]]):
        N = len(mat)
        dp = [[0]* N] * N
        result = -1
        for row in range(N - 1, -1, -1):
            for col in range(N - 1, -1, -1):
                if row == col == N - 1:
                    dp[row][col] = mat[-1][-1]
                elif row == N - 1:
                    dp[row][col] = max(mat[row][col], dp[row][col + 1])
                elif col == N - 1:
                    dp[row][col] = max(mat[row][col], dp[row + 1][col])
                else:
                    result = max(result, dp[row + 1][col + 1] - mat[row][col])
                    dp[row][col] = max(mat[row][col], dp[row + 1][col],dp[row][col + 1])
        return result
    
    
sol = Solution()
mat = [ [  1, 2, -1, -4, -20 ] ,
             [  -8, -3, 4, 2, 1 ] , 
             [  3, 8, 6, 1, 3 ] ,
             [  -4, -1, 1, 7, -6 ] ,
             [  0, -4, 10, -5, 1 ] ] 
print(sol.findMaxValuePair(mat))