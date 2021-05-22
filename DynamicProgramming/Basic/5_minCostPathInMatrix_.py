mat=[
    [1,2,3],
    [4,8,2],
    [1,5,3],
     ]






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
            # print(dp)
            
            col-=1
        row-=1
    return dp[0][0],dp
def minCostPath_Rec(mat,row,col,psf,memo_dict={}):
    x=str(row)+"-"+str(col)
    if x in memo_dict:
        return memo_dict[x]
    if row<0 or col<0 or row>=len(mat) or col>=len(mat[0]):
        return 0
    from_down=minCostPath_Rec(mat,row+1,col,psf+"D")
    from_right=minCostPath_Rec(mat,row,col+1,psf+"R")
    print(row,col)
    if from_down==0:
        memo_dict[x]=from_right+mat[row][col]
        return from_right+mat[row][col]
    elif from_right==0:
        memo_dict[x]=from_down+mat[row][col]
        return from_down+mat[row][col]
    memo_dict[x]=min(from_down,from_right)+mat[row][col]
    return memo_dict[x]
print(minCostPath(mat))
print(minCostPath_Rec(mat,0,0,""))