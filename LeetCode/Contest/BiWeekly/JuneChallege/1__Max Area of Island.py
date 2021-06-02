from typing import List


class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """visited=[[False]*len(grid[0]) for _ in range(len(grid))]"""
        
        def exploreNeighbours(row,col):
            dr=[-1,+1,0,0]
            dc=[0,0,-1,+1]
            count_=1
            for i in range(4):
                rr=row+dr[i]
                cc=col+dc[i]
                if rr<0 or cc<0 or rr>=len(grid) or cc>=len(grid[0]):
                    continue
                if grid[rr][cc]==0:
                    continue
                count_+=dfs(rr,cc)
            return count_
        
        def dfs(rr,cc):
            grid[rr][cc]=0
            return exploreNeighbours(rr,cc) 
        
        max_=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    max_=max(dfs(row,col),max_)
        return max_
    
sol=Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid= [[0,0,0,0,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))
                    