

def searchInarr(arr,left,right):
    if(len(arr)==0):
        return -1+1
    if(len(arr)==1):
        if(arr[0]==1):
            return 0
        return -1+1
    mid=(left+right)//2
    if(left>right):
        return -1+1
    if(arr[mid]==1 and arr[mid+1]==0):
        return mid+1
    else:
        if(arr[mid]==0):
            return searchInarr(arr,0,mid-1)
        else:
            return searchInarr(arr,mid+1,right)

        
        

        
        
    
