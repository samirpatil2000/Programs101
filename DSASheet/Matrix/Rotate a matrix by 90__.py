from typing import List


class Solution:
    
    def findMaxValuePair(self, mat:List[List[int]]):
        N = len(mat)
        
        for row in range(N):
            for col in range(row + 1):
                mat[row][col], mat[col][row] =  mat[col][row], mat[row][col]
        
        for row in range(N):
            for col in range(N//2):
                mat[row][col], mat[row][N - col - 1] =  mat[row][N - col - 1], mat[row][col]
        return mat
sol = Solution()
mat = [ [  1, 2, -1, -4, -20 ] ,
             [  -8, -3, 4, 2, 1 ] , 
             [  3, 8, 6, 1, 3 ] ,
             [  -4, -1, 1, 7, -6 ] ,
             [  0, -4, 10, -5, 1 ] ] 
mat = arr = [ [ 1, 2, 3, 4 ],
                    [ 5, 6, 7, 8 ],
                    [ 9, 10, 11, 12 ],
                    [ 13, 14, 15, 16 ] ]
print(sol.findMaxValuePair(mat))