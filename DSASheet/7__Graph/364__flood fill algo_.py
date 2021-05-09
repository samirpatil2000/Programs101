# https://leetcode.com/problems/flood-fill/

mat=[[1, 1, 0, 0],
     [1, 1, 0, 1],
     [1, 1, 0, 0],
     [0, 1, 1, 1]]

mat=[[0,0,0],[0,0,0]]


def exploarNeighbours(mat,sr,sc,visited,newcolor,oldColour):
    dr=[-1,+1,0,0]
    dc=[0,0,-1,+1]
    
    for i in range(4):
        rr=sr+dr[i]
        cc=sc+dc[i]
        if rr>=len(mat) or cc>=len(mat[0]):
            continue
        if rr<0 or cc<0:
            continue
        if visited[rr][cc]:
            continue
        if mat[rr][cc]!=oldColour:
            continue
        flood_fill(mat,rr,cc,visited,newcolor,oldColour)

def flood_fill(mat,sr,sc,visited,newcolor,oldColour):
    visited[sr][sc]=True
    mat[sr][sc]=newcolor
    exploarNeighbours(mat,sr,sc,visited,newcolor,oldColour)
    
visited=[[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
flood_fill(mat,0,0,visited,2,mat[0][0])
print(mat)