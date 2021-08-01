
def nums_(nums):
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if(nums[i]==nums[j]):
                count+=1
    return count

ls=[1,2,3]
print(nums_(ls))