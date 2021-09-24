def numberOfPaths(mat):
    n=len(mat)
    m=len(mat[0])

    count = [[0 for _ in range(m)] for _ in range(n)]
   
    mod=10**9+7
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):  
            if mat[i][j] == 1: 
                if i==n-1 or j==m-1:
                    count[i][j] = 1
                else:                    
                    count[i][j] = count[i+1][j] + count[i][j+1]
            else:
                count[i][j]=0
        print(count)
    return count[0][0]%mod




mat=[[1,1,0,1],
     [1,1,1,1]]

# mat=[[1,1,1,1],
#      [1,1,1,1],
#      [1,1,1,1]]

[[2, 1, 0, 1], 
 [1, 1, 1, 1]]
# [[10, 6,  3, 1], 
#  [4 ,3, 1+1, 1], 
#  [1 , 1, 1, 1]]


# mat=[[1,1],[0,1]]
# mat=[1]
print(numberOfPaths(mat))


