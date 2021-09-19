


def bfs(grid,maxTime):
    queue=[[0,0]]
    visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    time=0
    while queue:
        current_row,current_col=queue.pop(0)
        dr=[-1,+1,0,0]
        dc=[0,0,-1,+1]
        if maxTime>=time and current_col==len(grid[0])-1 and current_row==len(grid)-1:
            return "Yes"
        if maxTime<time:
            return "No"
        visited[current_row][current_col]=True
        time+=1
        for i in range(4):
            rr=current_row+dr[i]
            cc=current_col+dc[i]
            if rr<0 or cc<0:
                continue
            if rr>=len(grid) or cc>=len(grid[0]):
                continue
            if visited[rr][cc]:
                continue
            if grid[rr][cc]=="#":
                continue
            queue.append([rr,cc])
    return "No"


grid=[[".",".","#","."],
      ["#",".","#","#"],
      ["#",".",".","."]]
grid=[[".","#"],
      ["#","."]]
maxtime=2
print(bfs(grid,maxtime))
            
        
        
        
            