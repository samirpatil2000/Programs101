


mat=[[1,1,1,1,0,1],
     [0,0,1,1,0,1],
     [0,1,1,1,1,1],
     [0,0,1,1,1,0],
     [0,0,1,1,0,0],
     [0,1,1,1,0,0],]


row=len(mat)
col=len(mat[0])
# print(row,col)


visited=[[False for j in range (col)] for i in range(row)]
m= visited


# print(visited)

def drawTreeComponent(mat,i,j,visited_arr):
    if(i<0 or j<0 or i>=len(mat) or j>=len(mat[0]) or mat[i][j]==1 or visited_arr[i][j]==True):
        return
    visited_arr[i][j]=True
    drawTreeComponent(mat,i+1,j,visited_arr)
    drawTreeComponent(mat,i-1,j,visited_arr)
    drawTreeComponent(mat,i,j+1,visited_arr)
    drawTreeComponent(mat,i,j-1,visited_arr)
    # print(visited_arr)

def function(mat,row,col,visited_arr):
    count=0
    for i in range(row):
        for j in range(col):
            if(mat[i][j]==0 and visited_arr[i][j]==False):
                drawTreeComponent(mat,i,j,visited_arr)
                count=count+1
    return count

x=function(mat,row,col,m)

print("The number of island is : ",x)
    