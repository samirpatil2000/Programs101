mat=[[2,2,2],[5,4,3]]
    #  [9,8,2]]






def goldMine(mat):
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
            elif(col==COL-1):
                dp[row][col]=mat[row][col]
            elif(row==ROW-1):
                dp[row][col]=mat[row][col]+max(dp[row][col+1],dp[row-1][col-1])
            elif(row==0):
                dp[row][col]=mat[row][col]+max(dp[row][col+1],dp[row+1][col+1])
            else:
                dp[row][col]=mat[row][col]+max(dp[row][col+1],max(dp[row+1][col+1],dp[row-1][col-1]))
            col-=1
        row-=1
    max_=dp[0][0]
    for i in range(len(mat)):
        if(max_<mat[i][0]):
            max_=mat[i][0]
    
    return max_


def goldMineMemo(mat,row,col,memo={}):
    x=str(row)+"-"+str(col)
    if x in memo:return memo[x]
    if row<0 or col<0 or row>=len(mat) or col>=len(mat[0]):return 0

    
    from_topRight=goldMineMemo(mat,row-1,col+1)
    from_bottomRight=goldMineMemo(mat,row+1,col+1)
    from_Right=goldMineMemo(mat,row,col+1)
    # print(row,col)
    
    memo[x]=max(from_topRight,from_bottomRight,from_Right)+mat[row][col]
    
    return memo[x]

    
    

print(goldMine(mat))
print(goldMineMemo(mat,0,0))