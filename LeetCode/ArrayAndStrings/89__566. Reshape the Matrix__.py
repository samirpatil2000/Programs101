from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat[0])*len(mat):return mat
        new_mat=[[0]*c for _ in range(r)]
        print(new_mat)
        new_row=0
        new_col=0
        for o_r in range(len(mat)):
            for o_c in range(len(mat[0])):
                new_mat[new_row][new_col]=mat[o_r][o_c]
                new_col+=1
                if new_col>=c:
                    new_col=0
                    new_row+=1
        
        return new_mat

sol=Solution()
mat = [[1,2],[3,4]]
r = 1
c = 4
# r = 2
# c = 4
print(sol.matrixReshape(mat,r,c))