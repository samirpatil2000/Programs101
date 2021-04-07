
def largestSubArray(arr,k):
    i=0
    j=0
    sum_=0
    max_=-2**32
    while(j<len(arr)):
        # if(sum_ < k):
        sum_+=arr[j]      
        if(sum_==k):
            max_=max(j-i+1,max_)
        elif(sum_>k):
            while(sum_>k):
                sum_-=arr[i]
                i+=1
        j+=1  
    return max_

arr=[4,1,5,2,1,1,1,1,1,0,2,3,4,1,1,1,1,0,0,0,1]
k=5
print(largestSubArray(arr,k))