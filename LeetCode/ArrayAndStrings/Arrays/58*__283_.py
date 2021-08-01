def moveZeroes(nums):
    print(nums)
    i=0
    while(i<len(nums)):
        j=i+1
        while(j<len(nums) and nums[j]==0):
            j+=1
        if(nums[i]==0 and j<len(nums) and nums[j]!=0):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        i+=1
            
    print(nums)
    
nums = [4,2,4,0,0,3,0,5,1,0]
moveZeroes(nums)
        
            