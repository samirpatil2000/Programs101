def findTarget(arr,target):
    low,high=0,len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        
        if (target==arr[mid]):
            return mid
        
        if(arr[low]<=arr[mid]):
            if(arr[low]<=target and target<arr[mid]):
                high=mid-1
            else:
                low=mid+1
        else:
            if(arr[mid]<target and target<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    
    return -1

nums = [3,1]
target = 1
# nums = [4,5,6,7,0,1,2]
# target = 0
print(findTarget(nums,target))