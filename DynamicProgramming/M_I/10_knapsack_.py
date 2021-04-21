
def knapsack(values,weights,n,target):
    dp=[[0 for _ in range(target+1)] for _ in range(n+1)]
    
    for row in range(1,n+1):
        for col in range(1,target+1):
            # if (row==0 and col==0):
            #     dp[row][col]=0
            # else:
            
            val=values[row-1]
            dp[row][col]=dp[row-1][col]
            if(col>=val):
                dp[row][col]=max(dp[row-1][col],weights[row-1]+dp[row-1][col-val])
                    
    
    print(dp)
    
arr=[2,5,1,3,4]
wt=[15,14,10,45,30]   
    
knapsack(arr,wt,len(arr),7)  
    