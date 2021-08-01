


def sortAnArray(nums):
    i=0
    j=len(nums)-1
    while(i<j):
        if nums[i]%2!=0 and nums[j]%2==0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        elif nums[i]%2==0:
            i+=1
        elif nums[j]%2!=0:
            j-=1
    print(nums)
    i=0
    j=len(nums)-1
    # print(j,nums[j])
    count=0
    while(i<j and count<20):
        print(i)
        if (i%2==0 and nums[i]%2==0) or (i%2!=0 and nums[i]%2!=0):
            i+=1
        elif (j%2==0 and nums[j]%2==0) or (j%2!=0 and nums[j]%2!=0):
            j-=1
        elif (i%2!=0 and nums[i]%2==0) or (i%2==0 and nums[i]%2!=0):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        count+=1
    return nums
        
    
            
arr=[1,2,3,3,2,3,0,4]

# arr=[3,2]
print(len(arr)//2)
print(sortAnArray(arr))
        
    