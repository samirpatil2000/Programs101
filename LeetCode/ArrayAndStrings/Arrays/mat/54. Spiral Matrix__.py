from typing import List


class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        bool=0
        n=len(mat)
        m=len(mat[0])
        start_row=start_col=0
        end_row=n-1
        end_col=m-1
        list_=[]
        while start_col<=end_col and start_row<=end_row:
            
            if bool%4==0:
                for col in range(start_col,end_col+1):list_.append(mat[start_row][col])
                print(bool)
                start_row+=1
                bool+=1
            elif bool%4==1:
                for row in range(start_row,end_row+1):list_.append(mat[row][end_col])
                print(bool)

                end_col-=1
                bool+=1
            elif bool%4==2:
                for col in range(end_col,start_col-1,-1):list_.append(mat[end_row][col])
                print(bool)

                end_row-=1
                bool+=1
            elif bool%4==3:
                for row in range(end_row,start_row-1,-1):list_.append(mat[row][start_col])
                print(bool)

                start_col+=1
                bool+=1
                    
        return list_
    
    
sol=Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(mat))