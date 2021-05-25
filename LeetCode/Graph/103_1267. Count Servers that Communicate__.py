from typing import Counter, List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        
        def dfs(row,col,count_):
            if row>=len(grid) or col>=len(grid[0]):
                return
            if visited[row][col]==True or grid[row][col]==0:
                return
            visited[row][col]=True
            count_[0]+=1
            # print(grid[row][col])
            for i in range(len(grid)):
                dfs(row+i,col,count_)
            for i in range(len(grid[0])):
                dfs(row,col+i,count_)
        result=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count_=[0]
                if visited[row][col]==False and grid[row][col]!=0:
                    dfs(row,col,count_)
                    # print(grid[row][col])
                    if count_[0]>1:
                        result+=count_[0]
                    # print(count_)
        return result
    
    def iterativeMethod(self, grid: List[List[int]]):
        
        if len(grid)==0 and len(grid[0])==0:
            return 0
        comps_per_row=[0]*len(grid)
        comps_per_col=[0]*len(grid[0])
        
        coordinates=[]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    coordinates.append([row,col])
                    comps_per_row[row]+=1
                    comps_per_col[col]+=1
        count_=0
        for row_,col_ in coordinates:
            if comps_per_col[col_]>1 or comps_per_row[row_]>1:
                count_+=1
                
        return count_
        


g=[[1,0],[0,1]]
sol=Solution()
print(sol.countServers(g))
print(sol.iterativeMethod(g))
                    