
def arrangeBuildings(n):
    dp0=[1]*(n+1)
    dp1=[1]*(n+1)
    
    for i in range(2,n+1):
        dp1[i]=dp1[i-1]+dp0[i-1]
        dp0[i]=dp1[i-1]
    return dp0[n]+dp1[n]


def arrangeBuildingsWithoutArray(n):
    dpB=1
    dpS=1
    
    for i in range(2,n+1):
        x=dpB
        dpB=dpS
        dpS=dpS+x
    return (dpB+dpS)**2

n=5
print(arrangeBuildings(n))
print(arrangeBuildingsWithoutArray(n))
    