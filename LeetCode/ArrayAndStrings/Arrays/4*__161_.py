def peak_Brute(nums):
    for i in range(1,len(nums)):
        if(i!=0 and i!=len(nums)):
            if(nums[i-1]<nums[i] and nums[i]>nums[i+1]):
                return i
            
            
ls=[1,2,1,3,5,6,4]
print(peak_Brute(ls))

def opt(nums,left,right):
    mid=(left+right)//2
    if(left==right):
        return left
    if(left>right):
        return -1
    if(left + 1 == right):
        if(nums[left]>nums[right]):
            return left
        return right
    
    if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
        return mid
    else:
        if(nums[mid+1]>nums[mid]):
            return opt(nums,mid+1,right)
        else:
            return opt(nums,left,mid-1)
    
print(opt(ls,0,len(ls)-1))
n=len(nums)
if(n==1): 
    return 0        
if(nums[0]>nums[1]): 
    return 0
if(nums[n-1]>nums[n-2]): 
    return n-1
        
        return binary_search(nums);