

def findMin(nums):
    low,high=0,len(nums)-1
    
    # count=0
    while(low<=high):
        mid=(low+high)//2
        print(nums[mid],mid,low,high)
        # mid=
        if (mid+1<len(nums) and nums[mid] >= nums[mid-1] and nums[mid]>nums[mid+1]):
            # print()
            return nums[mid+1]
        elif(nums[mid] >= nums[mid-1] and mid+1==len(nums)):
            return nums[0]
        if (nums[mid]>=nums[0]):
            low=mid+1
        else:
            high=mid-1
        # count+=1
    return -1


nums= [3,2]
print(findMin(nums))