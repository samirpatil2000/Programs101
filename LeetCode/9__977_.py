
def sortedSq(nums):
    left=0
    right=len(nums)-1
    res=[]
    while(left<=right):
        if(abs(nums[left])>abs(nums[right])):
            res.append(nums[left]*nums[left])
            left+=1
        else:
            res.append(nums[right]*nums[right])
            right-=1
    res.reverse()
    return res

nums = [-4,-1,0,3,10]
print(sortedSq(nums))
            
            
        
    