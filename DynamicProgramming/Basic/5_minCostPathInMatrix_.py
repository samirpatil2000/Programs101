mat=[[2,2,3],[3,4,1]]
    #  [9,8,2]]






def minCostPath(mat):
    dp=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    # print(dp)
    print(mat)
    
    row=len(mat)-1
    COL=len(mat[0])
    ROW=len(mat)
    
    while(row >=0):
        col=len(mat[0])-1
        while(col >=0):
            if(row==ROW-1 and col==COL-1):
                dp[row][col]=mat[row][col]
            elif(row==ROW-1):
                dp[row][col]=mat[row][col]+dp[row][col+1]
            elif(col==COL-1):
                dp[row][col]=mat[row][col]+dp[row+1][col]
            else:
                dp[row][col]=mat[row][col]+min(dp[row+1][col],dp[row][col+1])
            print(dp)
            
            col-=1
        row-=1
    return dp[0][0],dp

print(minCostPath(mat))