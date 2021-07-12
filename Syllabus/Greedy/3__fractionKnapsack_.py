
a=[
    [40,5],
    [21,7],
    [24,4],
    [12,6],
    [30,6],
    ]



def fractionKnapsack(arr,X):
    arr.sort(key=lambda arr:arr[0]/arr[1],reverse=True)
    i=0
    price_=0
    sum_=0
    while(sum_<=X and i<len(arr)):
        if arr[i][1]<=X and sum_+arr[i][1]<=X:
            # X=X-arr[i][1]
            sum_+=arr[i][1]
            price_+=arr[i][0]
            print(sum_,price_)
        else:
            sum_+arr[i][1]
        i+=1
        
    return price_
            
        
    
print(fractionKnapsack(a,20))
    