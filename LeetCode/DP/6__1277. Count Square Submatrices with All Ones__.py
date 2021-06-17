from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROW=len(matrix)
        COL=len(matrix[0])
        
        dp=[[0]*COL for _ in range(ROW)]
        count_=0
        for row in range(ROW):
            for col in range(COL):
                if row==0 or col==0:
                    dp[row][col]=matrix[row][col]
                    if dp[row][col]==1:
                        count_+=1
                else:
                    if matrix[row][col]==1:
                        dp[row][col]=min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1
                        count_+=dp[row][col]
                    else:
                        dp[row][col]=0
        return count_
    
    
sol=Solution()
matrix =[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
matrix=[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(sol.countSquares(matrix))
                    
                # if dp[row][col]==1:
                    