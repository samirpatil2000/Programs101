def candies(nums,extraCandies):
    n=len(nums)
    bool_arr=[False for _ in range(n)]
    max_=nums[0]
    for i in range(1,n):
        if(nums[i]>max_):
            max_=nums[i]
    for i in range(0,n):
        if(nums[i]+extraCandies >= max_):
            bool_arr[i]=True
    return bool_arr

ls=[4,2,1,1,2]
print(candies(ls,1))