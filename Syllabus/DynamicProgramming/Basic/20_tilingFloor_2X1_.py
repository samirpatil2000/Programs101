
def tilling_2X1(n):
    dp=[None for _ in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


print(tilling_2X1(4))
    