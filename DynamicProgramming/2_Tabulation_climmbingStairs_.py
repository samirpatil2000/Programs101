

def countPathsDynamic(n,qb):
    if(n==0):
        return 1
    elif(n<0):
        return 0
    count=0
    # print("Hello ",n)
    if(qb[n]!=0):
        return qb[n]
    count+=countPathsDynamic(n-1,qb)
    count+=countPathsDynamic(n-2,qb)
    count+=countPathsDynamic(n-3,qb)
    
    qb[n]=count
    
    
    return count

def countPathsTabular(n):
    arr=[0 for _ in range(n+1)]
    arr[0]=1
    for i in range(1,n+1):
        print(arr[i])
        if(i==1):
            arr[i]=arr[i-1]
        elif(i==2):
            arr[i]=arr[i-1]+arr[i-2]
        else:
            arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
    return arr[n],arr
    
n=10
qb=[0]*(n+1)
y=countPathsDynamic(n,qb)
z=countPathsTabular(n)
print(y,z)