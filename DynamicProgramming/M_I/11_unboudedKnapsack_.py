
def unbounded(values,weight,target,n):
    dp=[0 for _ in range(target+1)]
    for i in range(target+1):
        max_=0
        for j in range(n):
            if (i>=values[j]):
                max_=max(dp[i-values[j]]+weight[j],max_)
        dp[i]=max_
    
    print(dp)
        
    # print(max_)

    
arr=[2,5,1,3,4]
wt=[15,14,10,45,30]   

unbounded(arr,wt,7,len(arr))