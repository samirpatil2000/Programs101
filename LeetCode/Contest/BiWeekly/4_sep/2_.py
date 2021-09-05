from typing import List


class Solution:
    def isValid(self,mat,row,col,visited)->bool:
        if row<0 or col<0 or row>=len(mat) or col>=len(mat[0]):
            return False
        if mat[row][col]==0 or (row,col) in visited:
            return False
        return True
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def explorNeighbours(mat,current_row,current_col,queue):
            dr=[-1,+1,0,0]
            dc=[0,0,-1,+1]
            for i in range(4):
                rr=current_row+dr[i]
                cc=current_col+dc[i]
                
                if rr<0 or cc<0:
                    continue
                if rr>=len(mat) or cc>=len(mat[0]):
                    continue
                if visited[rr][cc]:
                    continue
                if mat[rr][cc]==1:
                    continue
                queue.append(rr,cc) 
                visited[rr][cc]=True
                
        def dfs(mat,row,col,visited:dict):
            visited[(row,col)]=True
            dir_x=[0,0,-1,1]
            dir_y=[-1,1,0,0]
            res=[(row,col)]
            # for i in range(4):
            #     new_row=row+dir_x[i]
            #     new_col=col+dir_y[i]
            #     if self.isValid(mat,new_row,new_col,visited):
            #         res+=dfs(mat,new_row,new_col,visited)[::-1]
            # return res
        visited={}
        result=[]
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col]==1 and (row,col) not in visited:
                    x=dfs(land,row,col,visited)
                    print(x)
                    if len(x)==1:
                        result.append([row,col,x[0][0],x[0][1]])
                    if len(x)>1:
                        result.append([row,col,x[-1][0],x[-1][1]])
        return result
    
    
sol=Solution()
land = [[1,0,0],[0,1,1],[0,1,1]]
land = [[1,1],[1,1]]
land = land = [[0]]
land=[[1,1,1,1,1,1,1,1,1,1,1,1]]

print(sol.findFarmland(land))