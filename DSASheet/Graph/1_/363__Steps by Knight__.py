# https://leetcode.com/problems/flood-fill/

N=6
mat=[[0 for _ in range(N)] for _ in range(N)]

def exploarNeighbours(mat,sr,sc,visited,row_queue,col_queue,path_):
    # dr=[-2,-2,+2,+2,-1,+1,-1,+1]
    # dc=[-1,+1,-1,+1,-2,-2,+2,+2]
    dr=  [2, 2, -2, -2, 1, 1, -1, -1]
    dc = [1, -1, 1, -1, 2, -2, 2, -2]
    
    for i in range(8):
        rr=sr+dr[i]
        cc=sc+dc[i]
        if rr>=len(mat) or cc>=len(mat[0]):
            continue
        if rr<0 or cc<0:
            continue
        if visited[rr][cc]:
            continue
        row_queue.append(rr)
        col_queue.append(cc)
        
        path_[0]+="("+str(rr)+str(cc)+")-->"
        
        

def minStepToReachTargetBFS(mat,sr,sc,visited,target_row,target_col):
    row_queue=[sr]
    col_queue=[sc]
    path_=["("+str(sr)+str(sc)+")-->"]
    
    while(row_queue):
        
        rr=row_queue.pop(0)
        cc=col_queue.pop(0)
        print(rr,cc)
        print(visited)
        if visited[rr][cc]==True:
            continue
        visited[rr][cc]=True
        if rr==target_row and cc==target_col:
            print(path_[0])
            print("We find is")
            return
        exploarNeighbours(mat,rr,cc,visited,row_queue,col_queue,path_)
        
    
    
    
visited=[[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
minStepToReachTargetBFS(mat,2,2,visited,0,5)
# print(mat)