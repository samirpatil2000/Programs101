

def slidingWindow(arr,k):
    n=len(arr)
    if(n<k):
        return -1
    sum_=sum(arr[:k])
    MAX=sum_
    
    for i in range(n-k):
        sum_=sum_-arr[i]+arr[i+k]
        MAX=max(MAX,sum_)
    
    return MAX

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 3
print(slidingWindow(arr,k))

    
    




