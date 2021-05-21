
def exploreNeighbours(mat,row,col,visited):
    dr=[+1,+1,+1,-1,-1,-1, 0, 0]
    dc=[ 0,+1,-1, 0,+1,-1,+1,-1]
    # print(visited)
    for i in range(8):
        rr=row+dr[i]
        cc=col+dc[i]
        if rr<0 or cc<0 or rr>=len(mat) or cc>=len(mat[0]):
            continue
        if visited[rr][cc]==True or mat[rr][cc]==0:
            continue
        get_island(mat,rr,cc,visited)
    
        
    
    

def get_island(mat,row,col,visited):
    visited[row][col]=True
    exploreNeighbours(mat,row,col,visited)
    
    
mat=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]


def count_island(mat):
    visited=[[False]*len(mat[0]) for _ in range(len(mat))]
    count=0
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if visited[row][col]==False and mat[row][col]==1:
                get_island(mat,row,col,visited)
                count+=1
    return count


print(count_island(mat))
        
    