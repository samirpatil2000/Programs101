
arr=[5,10,20,100,7,6]

def maxSum(arr):
    include_dp=arr[0]
    exclude_dp=0
    for i in range(1,len(arr)):
        temp_include=include_dp
        include_dp=exclude_dp+arr[i]
        exclude_dp=max(temp_include,exclude_dp)
    return max(include_dp,exclude_dp)


print(maxSum(arr))


def maxSumNonAdj(arr,index,is_prev,psf):
    if index>len(arr):return
    if index==len(arr):
        print(psf)
        return
    
    if is_prev:
        maxSumNonAdj(arr,index+1,is_prev=False,psf=psf)
    else:
        maxSumNonAdj(arr,index+1,is_prev=False,psf=psf)
        maxSumNonAdj(arr,index+1,is_prev=True,psf=psf+arr[index])

maxSumNonAdj(arr,0,False,0)
        
    
        