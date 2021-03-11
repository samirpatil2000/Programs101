def runningSum(nums):
    res=[0 for _ in range(len(nums))]
    res[0]=nums[0]
    for i in range(1,len(nums)):
        res[i]=res[i-1]+nums[i]
    return res

nums=[3,1,2,10,1]

print(runningSum(nums))