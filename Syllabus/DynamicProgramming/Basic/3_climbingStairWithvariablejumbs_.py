

def climbingStair(n,jumps):
    arr=[0]*n
    arr[n-1]=1
    
    i=n-2
    while(i>=0):
        print(i)
        k=1
        while(i<n-k and k<=jumps[i]):
            arr[i]+=arr[i+k]
            k+=1
        i-=1
    return arr


n=7
jumps=[2,3,0,2,2,3]

print(climbingStair(n,jumps))

