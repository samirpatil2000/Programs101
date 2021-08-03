from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dr,dc=[-1,+1,0,0],[0,0,-1,+1]
        def dfs(current_row,current_col,idx):
            grid[current_row][current_col]=idx
            count_=1
            for i in range(4):
                row=current_row+dr[i]
                col=current_col+dc[i]
                if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):continue
                if grid[row][col]!=1:continue
                count_+=dfs(row,col,idx)
            return count_
                
        idx=2
        area={}
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    a=dfs(row,col,idx)
                    if idx not in area:
                        area[idx]=a
                    idx+=1
                    
        if len(area)==0:
            return 1
        max_area=area[2]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==0:
                    area_set,sum_=set(),1
                    for i in range(4):
                        current_row=row+dr[i]
                        current_col=col+dc[i]
                        if (current_row<0 or current_col<0 or current_col>=len(grid) or current_row>=len(grid[0])):continue
                        if grid[current_row][current_col]==0:continue
                        if grid[current_row][current_col] in area_set:continue
                        area_set.add(grid[current_row][current_col])
                        sum_+=area[grid[current_row][current_col]]
                    max_area=max(max_area,sum_)
        return max_area
        
        
sol=Solution()
grid=[[1,1,0,0],
      [0,1,1,0],
      [0,1,0,0],
      [1,0,1,0]]

grid = [[1,0],[0,1]]
grid = [[1,1],[1,1]]
# grid = [[1,1],[1,0]]
grid=[[0,0],[0,0]]
print(sol.largestIsland(grid))