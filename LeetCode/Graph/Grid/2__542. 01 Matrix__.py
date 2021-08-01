from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=[]
        n=len(mat)
        m=len(mat[0])
        for row in range(n):
            for col  in range(m):
                if mat[row][col]==0:
                    queue.append((row,col))
                else:
                    mat[row][col]=-1
                    
        dr=[-1,+1,0,0]
        dc=[0,0,-1,+1] 
        length=0
        while queue:
            length+=1
            for _ in range(len(queue)): 
                row,col=queue.pop(0)           
                for i in range(4):
                    new_row=row+dr[i]
                    new_col=col+dc[i]
                    if new_row<0 or new_row>=n or new_col<0 or new_col>=m or mat[new_row][new_col]!=-1:continue
                    mat[new_row][new_col]=length
                    queue.append((new_row,new_col))
        return mat
    
sol=Solution()
mat=[[0,0,0],[0,1,0],[0,0,0]]
# mat=[[0,0,0],[0,1,0]]
# mat=[[0,0,0],[0,1,0],[1,1,1]]
# mat=[[1,1,1],[1,1,1],[1,0,1]]
# mat=[[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]

print(sol.updateMatrix(mat))     
