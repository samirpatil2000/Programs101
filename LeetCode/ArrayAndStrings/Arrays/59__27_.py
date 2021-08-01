def FunctionName(nums,val):
    i=0
    j=len(nums)-1
    count=0
    while(i<=j):
        if(nums[i]!=val):
            i+=1   
        elif(nums[j]==val):
            j-=1
            count+=1
        elif(nums[i]==val and nums[j]!=val):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
            count+=1   
    print(nums)   
    return len(nums)-count

nums = [0,1,2,2,3,0,4,2]
val = 2
print(FunctionName(nums,val))