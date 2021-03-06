mat=[[0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0],]

N=5
arr = [[0 for i in range(N)] for i in range(N)]


def displayChess(chess,N):
    for i in range(N):
        for j in range(N):
            print(chess[i][j],end=" ")
        print()

def knightTours(chess,row,col,count,N):
    
    if(row>=N or col>=N or row<0 or col<0 or chess[row][col]!=0):
        return
    elif(count==(N-1)*(N-1)):
        chess[row][col]=count
        displayChess(chess,N)
        chess[row][col]=0
        return
    
    chess[row][col]=count
    knightTours(chess,row-2,col+1,count+1,N)
    knightTours(chess,row-1,col+2,count+1,N)
    knightTours(chess,row+1,col+2,count+1,N)
    knightTours(chess,row+2,col+1,count+1,N)
    knightTours(chess,row+2,col-1,count+1,N)
    knightTours(chess,row+1,col-2,count+1,N)
    knightTours(chess,row-1,col-2,count+1,N)
    knightTours(chess,row+2,col-1,count+1,N)
    chess[row][col]=0

knightTours(mat,5,2,1,7)
# displayChess(mat,7)