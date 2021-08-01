from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        dict_=set()
        for i in range(n-2):
            
                new_target=-nums[i]
                left=i+1
                right=n-1
                while left<right:
                    if nums[left]+nums[right]>new_target:
                        right-=1
                    elif nums[right]+nums[left]<new_target:
                        left+=1
                    else:
                        x=(nums[i],nums[left],nums[right])
                        if x not in dict_:
                            dict_.add(x)
                        left+=1
                        right-=1
        return [list(i) for i in dict_]
    
sol=Solution()
nums=[-1,0,1,2,-1,-4]
nums=[]
nums=[0]

print(sol.threeSum(nums))