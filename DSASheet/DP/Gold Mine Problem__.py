from copy import deepcopy
from typing import List


class Solution:
    def maxGold(self, n, m, M:List[List[int]]):
        if m == 1:
            return max(M)[0]
        if n == 1:
            return sum(M[0])
            
        dp = [[0] * m for _ in range(n)]
        max_ = 0
        for col in range(m):
            for row in range(n):
                dp[row][col] += M[row][col]
                if col == 0:
                    continue
                elif row == 0:
                    dp[row][col] += max(dp[row][col - 1], dp[row + 1][col - 1])
                elif row == n - 1:
                    dp[row][col] += max(dp[row][col - 1], dp[row - 1][col - 1])
                else:
                    dp[row][col] += max(dp[row][col - 1], dp[row + 1][col - 1], dp[row - 1][col - 1])   
                max_ = max(max_, dp[row][col])
        print(dp)
        for i in dp:
            print(i)
        return max_
    
sol = Solution()
n = 3
m = 3
M = [[1, 3, 3] ,
     [2, 1, 4] ,
     [0, 6, 4] ] ;

n = 4
m = 4
M =  [[1, 3, 1, 5] ,
      [2, 2, 4, 1] ,
      [5, 0, 2, 3] ,
      [0, 6, 1, 2] ] ;
n = 1
m =2
M = [[1, 2]]
print(sol.maxGold(n, m, M))
                
            