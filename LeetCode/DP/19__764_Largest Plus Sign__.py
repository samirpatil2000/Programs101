from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mat=[[1]*n for _ in range(n)]
        for i,j in mines:mat[i][j]=0
        up,down,left,right=[[1]*n for _ in range(n)],[[1]*n for _ in range(n)],[[1]*n for _ in range(n)],[[1]*n for _ in range(n)]
        #right
        for row in range(n):
            count_one=0
            for col in range(n):
                if mat[row][col]==1:count_one+=1
                else:count_one=0
                right[row][col]=count_one
        #down
        for col in range(n):
            count_one=0
            for row in range(n):
                if mat[row][col]==1:count_one+=1
                else:count_one=0
                down[row][col]=count_one
        #left
        for row in range(n):
            count_one=0
            for col in range(n-1,-1,-1):
                if mat[row][col]==1:count_one+=1
                else:count_one=0
                left[row][col]=count_one
        #up
        for col in range(n):
            count_one=0
            for row in range(n-1,-1,-1):
                if mat[row][col]==1:count_one+=1
                else:count_one=0
                up[row][col]=count_one
                
        result=0
        for row in range(n):
            for col in range(n):
                result=max(result,min(down[row][col],up[row][col],left[row][col],right[row][col]))
        return result
    
sol=Solution()
n,mines=5,[[3,0],[4,2],[0,4]]
# n,mines=1,[[0,0]]
n,mines=5, [[4,2]]

print(sol.orderOfLargestPlusSign(n,mines))