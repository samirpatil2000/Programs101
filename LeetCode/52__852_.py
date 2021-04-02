

def searchFun(arr,left,right):
    mid=(left+right)//2
    if(left>right):
        return -1
    if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
        return mid
    else:
        if(mid<len(arr)-1 and arr[mid]<arr[mid+1]):
            return searchFun(arr,mid+1,right)
        elif(mid<len(arr)-1 and arr[mid]>arr[mid+1]):
            return searchFun(arr,left,mid-1)


def peakIndexInMountainArray(arr):
    if(len(arr)==0):
        return
    if(len(arr)==1):
        return 0
    return searchFun(arr,0,len(arr))


arr =  [2]
print(peakIndexInMountainArray(arr))