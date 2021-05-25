from typing import List
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        updated_mat = [[-1] * len(isWater[0]) for _ in range(len(isWater))]
        print(isWater)
        print(updated_mat)
        
        q=[]
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col]==1:
                    q.append([row,col])
                    updated_mat[row][col]=0
        dr=[-1,+1,0,0]
        dc=[0,0,-1,+1]
        DIR = [0, 1, 0, -1, 0]
        while q:
            row_,col_=q.pop(0)
            for i in range(4):
                n_row,n_col=row_+dr[i],col_+dc[i]
                if n_row<0 or n_row==len(updated_mat) or n_col<0 or n_col==len(updated_mat[0]) or updated_mat[n_row][n_col]!=-1:
                    continue
                updated_mat[n_row][n_col]=updated_mat[row_][col_]+1
                q.append([n_row,n_col])
        return updated_mat
            
            

sol=Solution()

isWater=[[0,0,1],[1,0,0],[0,0,0]]
print(sol.highestPeak(isWater))