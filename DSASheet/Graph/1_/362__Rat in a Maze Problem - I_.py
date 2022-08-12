from types import resolve_bases


mat=[[1, 1, 0, 0],
     [1, 1, 0, 1],
     [1, 1, 0, 0],
     [0, 1, 1, 1]]


def explorNeighbours(mat,current_row,current_col,visited,path):
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
        if mat[rr][cc]==0:
            continue
        dfs(mat,rr,cc,visited,path+str(rr)+str(cc)+"-")
        
        
        
def dfs(mat,src_row,src_col,visited,path): 
    if src_row==len(mat)-1 and src_col==len(mat[0])-1:
        print(path)
        return
    visited[src_row][src_col]=True
    explorNeighbours(mat,src_row,src_col,visited,path)
    visited[src_row][src_col]=False
     


def explorNeighboursBFS(mat,current_row,current_col,visited,row_queue,col_queue):
    dr=[-1,+1,0,0]
    dc=[0,0,-1,+1]
    dir_ = [[-1, 0, "U"], [1, 0, "D"], [0, -1, "L"], [0, 1, "R"]]
    for i in range(4):
        rr=current_row + dr[i]
        cc=current_col + dc[i]
        
        if rr<0 or cc<0:
            continue
        if rr>=len(mat) or cc>=len(mat[0]):
            continue
        if visited[rr][cc]:
            continue
        if mat[rr][cc]==0:
            continue
        row_queue.append(rr)
        col_queue.append(cc)
        visited[rr][cc]=True
        
def bfs(mat,src_row,src_col,visited):
    row_queue=[src_row]
    col_queue=[src_col]
    visited[src_row][src_col]=True
    path_=""
    while(len(row_queue)>0):
        # print(row_queue,col_queue)
        rr_=row_queue.pop(0)
        cc_=col_queue.pop(0)
        path_+=str(rr_)+str(cc_)+"-"
        if rr_==len(mat)-1 and cc_==len(mat[0])-1:
            print(path_)
            # print("sa")
            return        
        # for i in range(rr_):
        explorNeighboursBFS(mat,rr_,cc_,visited,row_queue,col_queue)
        # visited[rr_][cc_]=False
            
visited=[[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
dfs(mat,0,0,visited,"00-")
# visited=[[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
# bfs(mat,0,0,visited)
    
    