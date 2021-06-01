from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        def dfs(row,col,side_A,side_B,side_D,side_C,sum_A,sum_B,sum_C,sum_D):
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):return
            
            dfs(row+1,col+1,side_A,side_B+1,side_C,side_D,sum_A,
                sum_B+grid[row][col]
                ,sum_C,sum_D)
            dfs(row+1,col-1,side_A+1,side_B,side_C,side_D,
                sum_A+grid[row][col],
                sum_B,sum_C,sum_D)
            
            dfs(row,col,side_A,side_B,side_C,side_D,sum_A,sum_B,sum_C,sum_D)
            dfs(row,col,side_A,side_B,side_C,side_D,sum_A,sum_B,sum_C,sum_D)