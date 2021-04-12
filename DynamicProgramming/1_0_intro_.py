

def fibo(n):
    if(n==0 or n==1):
        return n
    print("Hello ",n)
    return fibo(n-1)+fibo(n-2)


def fiboDynamic(n,qb):
    if(n==0 or n==1):
        return n
    if(qb[n]!=0):
        return qb[n]
    ans=fiboDynamic(n-1,qb)+fiboDynamic(n-2,qb)
    qb[n]=ans
    print("Hello ",n,qb[n])
    return ans


n=20
# print(fibo(n))
qb=[0]*(n+1)
# print(qb)
print(fiboDynamic(n,qb))
print(qb)


def countPaths(n):
    if(n==0):
        return 1
    elif(n<0):
        return 0
    count=0
    print("Hello ",n)
    count+=countPaths(n-1)
    count+=countPaths(n-2)
    count+=countPaths(n-3)
    
    return count



def countPathsDynamic(n,qb):
    if(n==0):
        return 1
    elif(n<0):
        return 0
    count=0
    print("Hello ",n)
    if(qb[n]!=0):
        return qb[n]
    count+=countPathsDynamic(n-1,qb)
    count+=countPathsDynamic(n-2,qb)
    count+=countPathsDynamic(n-3,qb)
    
    qb[n]=count
    
    
    return count
m=10
x=countPaths(m)
print("-")
qb=[0]*(m+1)
y=countPathsDynamic(m,qb)
print(x,y)