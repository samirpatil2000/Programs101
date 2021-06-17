from typing import List


class Solution:
    def querySum(self,prefix_sum:List[List[int]],start_row:int,start_col:int,end_row:int,end_col:int)->int:
        if start_row==0 and start_col==0:
            sum_=prefix_sum[end_row][end_col]
            return sum_
        elif start_row==0:
            sum_=prefix_sum[end_row][end_col]
            sum_-=prefix_sum[end_row][start_col-1]
            return sum_
        elif start_col==0:
            sum_=prefix_sum[end_row][end_col]
            sum_-=prefix_sum[start_row-1][end_col]
            return sum_
        else:
            sum_=prefix_sum[end_row][end_col]
            sum_-=prefix_sum[start_row-1][end_col]
            sum_-=prefix_sum[end_row][start_col-1]
            sum_+=prefix_sum[start_row-1][start_col-1]
            return sum_
        
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_sum=mat.copy()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row==0 and col==0:
                    prefix_sum[row][col]=mat[row][col]
                elif row==0:
                    prefix_sum[row][col]=prefix_sum[row][col-1]+mat[row][col]
                elif col==0:
                    prefix_sum[row][col]=prefix_sum[row-1][col]+mat[row][col]
                else:
                    prefix_sum[row][col]=prefix_sum[row][col-1]+prefix_sum[row-1][col]+mat[row][col]
                    prefix_sum[row][col]-=prefix_sum[row-1][col-1]
        result_mat=[[0]*len(mat[0]) for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                start_row=max(0,row-k)
                start_col=max(0,col-k)
                end_row=min(len(mat)-1,row+k)
                end_col=min(len(mat[0])-1,col+k)
                result_mat[row][col]=self.querySum(prefix_sum,start_row,start_col,end_row,end_col)
                
        return result_mat

        
        
        
        
    
    
sol=Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(sol.matrixBlockSum(mat,k))
[[12, 21, 16], [27, 45, 33], [24, 39, 26]]
[[12,21,16],[27,45,33],[24,39,28]]