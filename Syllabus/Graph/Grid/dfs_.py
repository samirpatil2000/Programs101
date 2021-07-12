


mat=[[0,1,0,1,0,1],
     [0,0,0,1,0,1],
     [0,1,0,0,0,1],
     [0,0,1,1,0,0],
     [0,0,0,1,0,0],
     [0,1,0,0,0,'E'],]


def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j],end=' ')
        print()
        
        
visited=[[False for _ in range(len(mat[0]))] for _ in range(len(mat))]

# def bfs(mat,):
row_queue=[]
col_queue=[]


def explorNeighbours(mat,current_row,current_col,visited):
    dr=[-1,+1,0,0]
    dc=[0,0,-1,+1]
    # list_=[]
    for i in range(4):
        rr=current_row+dr[i]
        cc=current_col+dc[i]
        
        if rr<0 or cc<0:
            continue
        if rr>=len(mat) or cc>=len(mat[0]):
            continue
        if visited[rr][cc]:
            continue
        if mat[rr][cc]==1:
            continue
        if dfs(mat,visited,rr,cc):
            return True
        
        
            
        
        
        
        

def dfs(mat,visited,src_row,src_col):
    visited[src_row][src_col]=True
    if mat[src_row][src_col]=='E':
        return True
    if explorNeighbours(mat,src_row,src_col,visited):
        return True
    
    return False


print(dfs(mat,visited,0,0))
    
    
    



