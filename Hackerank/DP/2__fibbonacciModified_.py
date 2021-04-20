


def fibonacciMod(n,t1,t2):
    if n==1:
        return t1
    elif n==2:
        return t2
    x=fibonacciMod(n-2,t1,t2)+(fibonacciMod(n-1,t1,t2)**2)
    
    return x



def fibonacciModDP(dp,n,t1,t2):
    if n==1:
        return t1
    elif n==2:
        return t2
    if dp[n]!=None:
        return dp[n]    
    x=fibonacciModDP(dp,n-2,t1,t2)+(fibonacciModDP(dp,n-1,t1,t2)**2)
    dp[n]=x
    return x

t1=0
t2=1
n=10

dp=[None for _ in  range(n+1)]
print(dp)
print(fibonacciModDP(dp,n,t1,t2))

# print(fibonacciMod(n,t1,t2))

