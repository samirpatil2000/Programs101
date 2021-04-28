
arr=[5,10,10,100,5,6]

def maxSum(arr):
    include_dp=arr[0]
    exclude_dp=0
    for i in range(1,len(arr)):
        temp_include=include_dp
        include_dp=exclude_dp+arr[i]
        exclude_dp=max(temp_include,exclude_dp)
    return max(include_dp,exclude_dp)


print(maxSum(arr))
        