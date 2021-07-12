


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


def explorNeighbours(mat,current_row,current_col):
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
    
        row_queue.append(rr)
        col_queue.append(cc) 
        
        visited[rr][cc]=True
        
path_count=0       
def bfs(mat,start_row,start_col):
    global path_count
    row_queue.append(start_row)
    col_queue.append(start_col)
    visited[start_row][start_col]
    
    while len(row_queue)>0: #or  len(col_queue)>0
        current_row=row_queue.pop(0)
        current_col=col_queue.pop(0)
        path_count+=1
        if mat[current_row][current_col]=='E':
            return True
        # go for neighbours
        explorNeighbours(mat,current_row,current_col)
        
        
    return False


print(bfs(mat,0,0),path_count)