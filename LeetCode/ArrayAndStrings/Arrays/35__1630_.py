


def function(nums, l_,r_):
    list_=nums[l_:r_+1]
    print(list_)
    list_.sort()
    print(list_)
    for k in range(len(list_)-1):
        if(list_[k+1] - list_[k] != list_[1] - list_[0]):
            return False
    return True

def checkArithmeticSubarrays(nums,l,r):
    list=[]
    for i in range(len(l)):
        list.append(function(nums,l[i],r[i]))
    return list

            
            
            
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10] 
print(checkArithmeticSubarrays(nums,l,r))