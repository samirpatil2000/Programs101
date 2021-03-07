
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
    
    
floodFill(mat,0,0,"")