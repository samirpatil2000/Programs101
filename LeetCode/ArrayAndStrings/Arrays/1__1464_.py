def maxProduct(nums):
    n=len(nums)
    max=-99
    for i in range(n-1):
        for j in range(i+1,n):
            val=(nums[i]-1)*(nums[j]-1)
            if(max<val):
                max=val
    return max

nums = [3,4,5,2]
print(maxProduct(nums))