def BruteForceRotateArray(nums,k):
    len_=len(nums)-1
    for i in range(k):
        
        print(nums,i)
        temp=nums[len_]
        i=len_-1
        while(i>=0):
            nums[i+1]=nums[i]
            i-=1
        nums[0]=temp


    
    
nums = [1,2,3,4,5,6,7]
k = 11

def reverseFunction(left,right):
    while(left<right):
        temp=nums[left]
        nums[left]=nums[right]
        nums[right]=temp
        left+=1
        right-=1

def rotateArray(nums,k):
    
    len_=len(nums)
    if(k>len_):
        k=k-len_
    reverseFunction(0,len_-1-k)
    # print(nums)
    reverseFunction(len_-1-k+1,len_-1)
    # print(nums)
    
    reverseFunction(0,len_-1)
    
    
    
    



print(nums)

            
        
rotateArray(nums,k)
print(nums) 