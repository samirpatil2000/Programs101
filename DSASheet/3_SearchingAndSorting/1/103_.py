def findTargetElement(self,arr,left,right,target):
    mid=(left+right)//2
    if(left>=right):
        return -1
    if(arr[mid]==target):
        return mid
    elif(arr[left] < arr[mid]):
        if(arr[left]<=target and arr[mid]>=target):
            return findTargetElement(arr,left,mid,target)
        else:
            return findTargetElement(arr,mid,right,target)
    else:
        if(arr[right]>=target and arr[mid]<=target):
            return findTargetElement(arr,mid,right,target)
        else:
            return findTargetElement(arr,left,mid,target)
    
            

def search(nums,target):
    n=len(nums)
    val=findTargetElement(nums,0,n-1,target)
    return val