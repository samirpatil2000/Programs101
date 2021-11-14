from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col=set(),set()
        n,m=len(matrix),len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        
        for i in row:
            for col_ in range(m):
                matrix[i][col_]=0

        for i in col:
            for row_ in range(n):
                matrix[row_][i]=0
    
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix),len(matrix[0])
        def makerowsandcolZero(row_:int,col_:int)->int:
            for j in range(m):
                matrix[row_][j]=0
            for j in range(n):
                matrix[j][col_]=0
            
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        for j in range(m):                
            if matrix[0][j]==0:
                makerowsandcolZero(0,j)
        for i in range(n):                
            if matrix[i][0]==0:
                makerowsandcolZero(i,0)
        
        
            

sol=Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# sol.setZeroes(matrix)
sol.setZeroes2(matrix)
print(matrix)