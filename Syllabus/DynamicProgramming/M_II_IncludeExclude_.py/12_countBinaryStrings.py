
def countBinaryStrings(n):
    dp0=[1]*(n+1)
    dp1=[1]*(n+1)
    
    for i in range(2,n+1):
        dp1[i]=dp1[i-1]+dp0[i-1]
        dp0[i]=dp1[i-1]
    return dp0[n]+dp1[n]


def countBinaryStringsWithoutArray(n):
    dp0=1
    dp1=1
    
    for i in range(2,n+1):
        x=dp0
        dp0=dp1
        dp1=dp1+x
    return dp0+dp1

n=5
print(countBinaryStrings(n))
print(countBinaryStringsWithoutArray(n))
    