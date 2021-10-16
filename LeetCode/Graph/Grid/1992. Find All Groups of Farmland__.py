from typing import List


class Solution:
    def isValid(self,mat,row,col,visited)->bool:
        if row<0 or col<0 or row>=len(mat) or col>=len(mat[0]):
            return False
        if mat[row][col]==0 or (row,col) in visited:
            return False
        return True
        
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        dr=[0,0,-1,1]
        dc=[-1,1,0,0]
        
        def dfs(mat,row,col,visited:dict):
            if self.isValid(mat,row,col,visited)==False:
                return [-2**32,-2**32]
            visited[(row,col)]=True
            x=max([dfs(mat,row+dc[i],col+dr[i],visited) for i in range(4)])
            return max(x,[row,col])
        
        visited={}
        result=[]
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col]==1 and (row,col) not in visited:
                    result.append([row,col]+dfs(land,row,col,visited))
        return result
    
sol=Solution()
land = [[1,1],[1,1]]
land = [[1,0,0],[0,1,1],[0,1,1]]
# land = [[1]]
print(sol.findFarmland(land))

# print(max([1,2],[1,1]))