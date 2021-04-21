def coinChangePermutation(coins,target):
    dp=[0 for _ in range(target+1)]
    dp[0]=1
    
    for i in range(1,len(dp)):
        for j in range(len(coins)):
            if (coins[j]<=i):
                dp[i]+=dp[i-coins[j]]
                
    
    print(dp)
    
    
coins=[2,3,5,6]  
coinChangePermutation(coins,10)
    