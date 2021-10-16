from typing import List
import heapq
class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:
        dr=[-1,+1,0,0]
        dc=[0,0,-1,+1]
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        
        queue=[[ grid[0][0],0,0 ]]
        heapq.heapify(queue)
        max_level=0
        print(len(grid) ,len(grid[0]))
        
        while queue:
            current_level,current_row,current_col=heapq.heappop(queue)
            max_level=max(max_level,current_level)
            visited[current_row][current_col]=True
            print(current_level,current_row,current_col)
            
            if current_row==len(grid)-1 and current_col==len(grid[0])-1:
                
                return max_level
            for i in range(4):
                row=current_row+dr[i]
                col=current_col+dc[i]
                
                if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):continue
                if visited[row][col]:continue
                
                heapq.heappush(queue,[grid[row][col],row,col])
                
        return max_level
    
    
sol=Solution()
grid=[[0,2],[1,3]]
grid=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(sol.swimInWater(grid))
                
        
        