
import sys
from sys import stdin, stdout

t = int(stdin.readline())
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())




def LShapedPlot(mat,R,C,row,col,row_count,col_count,output_str):
    if(row>=R or col>=C ):
        return
    if(mat[row][col]==0 or mat[row][col]==2 ):
        return
    if(row_count!=1 and col_count!=1 and row_count==(col_count)*2):
        print("count",output_str+"c")
        return
    if(row == R-1 and col == C-1):
        print(output_str)
        return
    temp=mat[row][col]
    mat[row][col]=2
    LShapedPlot(mat,R,C,row+1,col,row_count+1,col_count,output_str+"r")
    LShapedPlot(mat,R,C,row,col+1,row_count,col_count+1,output_str+"c")
    mat[row][col]=temp
    # print(temp)
    print(row_count,col_count)
    
    
    

for _ in range(t):
    R,C=get_ints()
    mat=[[None for _ in range(C)] for _ in range(R)]
    for i in range(R): 
        arr = [int(x) for x in stdin.readline().split()]
        for k in range(len(arr)):
            mat[i][k]=arr[k]
    print(mat)
    # print(mat)
    # LShapedPlot(mat,R,C,0,0,1,1,"")
    
    
    

    
    
"""
1
4 3
1 0 0
1 0 1
1 0 0
1 1 0
1
6 4
1 0 0 0
1 0 0 1
1 1 1 1
1 0 1 0
1 0 1 0
1 1 1 0

"""