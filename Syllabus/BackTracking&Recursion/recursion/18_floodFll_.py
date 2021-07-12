
mat=[[0,1,0,1,0,1],
     [0,0,0,1,0,1],
     [0,1,0,1,0,1],
     [0,0,1,1,0,0],
     [0,0,0,1,0,0],
     [0,1,0,0,0,0],]


def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=' ')
        print()

mat1=[[0,0,0],
      [0,1,0],
      [0,0,0],]


visited=[]

def floodFill(mat,row,col,output_str):
    if(row == len(mat)-1 and col == len(mat[0])-1):
        print(output_str)
        return
    if(row < 0 or col < 0 or row == len(mat) or col == len(mat[0]) or mat[row][col]==1 or mat[row][col]==2 ): 
        return
    # if(row < 0 or col <0 or row > n or col > m or mat[row][col]==1)
    temp=mat[row][col]
    mat[row][col]=2
    # printMat(mat)
    floodFill(mat,row+1,col,output_str+"d")
    floodFill(mat,row-1,col,output_str+"t")
    floodFill(mat,row,col+1,output_str+"r")
    floodFill(mat,row,col-1,output_str+"l")
    mat[row][col]=temp
    
    
# floodFill(mat,0,0,"")

def LShapedPlot(mat,R,C,row,col,row_count,col_count,output_str):
    if(row>=R or col>=C ):
        return
    if(mat[row][col]==1 or mat[row][col]==2 ):
        return
    if(row_count!=0 and col_count!=0 and row_count*2==col_count):
        print(output_str)
        return
    if(row == R-1 and col == C-1):
        # print(output_str)
        return
    temp=mat[row][col]
    mat[row][col]=2
    LShapedPlot(mat,R,C,row+1,col,row_count+1,col_count,output_str+"r")
    LShapedPlot(mat,R,C,row,col+1,row_count,col_count+1,output_str+"c")
    mat[row][col]=temp
    
# LShapedPlot(mat,len(mat),len(mat[0]),0,0,0,0,"r")