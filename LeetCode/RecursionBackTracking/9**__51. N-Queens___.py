from typing import List


class Solution:
    def isValid(self,mat,row,col,n):
        for c_row in range(row-1,-1,-1):
            if mat[c_row][col]=='Q':
                return False
            
        new_row=row-1
        new_col=col-1
        while new_row>=0 and new_col >=0:
            if mat[new_row][new_col]=='Q':
                return False
            new_row-=1
            new_col-=1
            
        new_row=row-1
        new_col=col+1
        
        while new_row>=0 and new_col<n:
            if mat[new_row][new_col]=='Q':
                return False
            new_row-=1
            new_col+=1
            
        return True
        
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat=[['.']*n for _ in range(n)]
        
        def solve(mat,row, col, n):
            if row==n:
                return [[''.join(mat[i]) for i in range(n)]]
            res=[]
            for col in range(n):
                if self.isValid(mat,row, col, n):
                    mat[row][col]='Q'
                    res+=solve(mat,row+1, col, n)
                    mat[row][col]='.'
                    # print(res)
            return res
        return solve(mat,0,0,n)
        
sol=Solution()
n=4

print(sol.solveNQueens(n))
a1=[]
a2=[1,2,3]
a3=[2,3]

print(a1+a2+a3)

a1.append(a2)
print(a1)