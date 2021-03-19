
def removeDuplicates(nums):
    i=count=0
    len_=len(nums)
    while(i<len_):
        j=i
        while(i+1<len_ and nums[i]==nums[i+1]):
            i+=1
        
       
        count+=1
        nums[count-1]=nums[i]
        # print(nums[count-1],nums[i])
        # print(nums)
        i+=1
    return count

nums = [1,1,2]
count=removeDuplicates(nums)
print(count)
print(nums[:count])