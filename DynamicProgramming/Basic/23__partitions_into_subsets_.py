

def partition_into_subset(n,k):
    dp=[[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(k):
        for j in range(n):
            if (j<i):
                dp[i][j]=0
            elif (j==i):
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+i*dp[i][j-1]


                
            
        
    