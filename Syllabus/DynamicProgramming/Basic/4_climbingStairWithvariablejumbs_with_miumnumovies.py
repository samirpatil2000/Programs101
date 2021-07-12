

def climbingStair(n,jumps):
    arr=[None]*n
    arr[n-1]=0
    # print(arr)
    
    i=n-2
    while(i>=0):
        k=1
        min_=2**32
        
        while(i<n-k and k<=jumps[i]):
            if(arr[i+k]!=None):
                min_=min(min_,arr[i+k])
            k+=1
        if(min_!=2**32):
            arr[i]=1+min_
        else:
            arr[i]=None
        i-=1
    return arr


n=10
jumps=[3,2,4,2,0,2,3,1,2,2]

print(climbingStair(n,jumps))

