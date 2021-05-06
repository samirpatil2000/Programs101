
def tilling_MX1(n,M):
    dp=[None for _ in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        if i>M:
            dp[i]=dp[i-1]+dp[i-M]
        else:
            dp[i]=dp[i-1]
    return dp[n]


print(tilling_MX1(4,5))
    