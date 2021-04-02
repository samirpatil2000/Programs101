

        
def linkedListCycledMethod(nums):
    if(len(nums)==2):
        return nums[0]
    slow=nums[0]
    fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if(slow==fast):
            print(slow,fast)
            break
        
    fast=nums[0]
    while(slow!=fast):
        print(fast,slow)
        slow=nums[slow]
        fast=nums[fast]
    return slow

def fu(nums):
    if(len(nums)==2):
        return nums[0]
    slow=nums[0]
    fast=nums[0]
    for _ in range(len(nums)):
        # print(fast,slow)
        slow=nums[slow]
        fast=nums[nums[fast]]
        if(slow==fast):
            # print(slow,fast)
            break
        
    fast=nums[0]
    while(slow!=fast):
        # print(fast,slow)
        slow=nums[slow]
        fast=nums[fast]
    return slow

nums =[1,1,2]
print(linkedListCycledMethod(nums))
print(fu(nums))