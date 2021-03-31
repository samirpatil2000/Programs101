# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid = [[-1]]



def countNegatives(grid):
    n=len(grid[0])
    col=n-1
    row=0
    count_=0
    while(col>=0 and row<len(grid)):
        # print(row,col,grid[row][col])
        if(grid[row][col]>=0):
            row+=1
        elif(grid[row][col]<0):
            if(grid[row][col-1]>=0 or col==0):
                # print(grid[row][col],n,col,row)
                # print(row,col,grid[row][col-1],"x")
                count_+=(n-col)
                row+=1
            elif(grid[row][col-1]<0):
                col-=1
    
    return count_



print(countNegatives(grid))