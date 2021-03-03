def isSafePlace(chess,row,col,N):
    for i in range(N):
        if(chess[i][col]==1):
            return False
    for i in range(N):
        if(chess[row][i]==1):
            return False
    k=0 
    while(k<N):
        if(chess[k][k]==1):
            return False
        k+=1
    i=N
    j=0
    while(i>=0 and j<N):
        if(chess[i][j]==1):
            return False
        i-=1
        j+=1
    return True
    
def printNQueens(chess,qsf,row,N):
    
    if(row==N):
        print(qsf)
        return
    for col in range(N):
        if(isSafePlace(chess,row,col,N)):
            chess[row][col]=1
            printNQueens(chess,qsf+str(row)+"-"+str(col)+",",row+1,N)
            chess[row][col]=0
    
mat=[[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],]

printNQueens(mat,"",0,6)