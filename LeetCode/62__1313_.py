
def decompressRLElist(nums):
    i=0
    new_arr=[]
    while(i<len(nums)):
        for _ in range(nums[i]):
            new_arr.append(nums[i+1])
        i+=2
        
    return new_arr


nums = [1,1,2,3]
print(decompressRLElist(nums))