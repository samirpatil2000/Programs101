from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        dict_=set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                new_target=target-(nums[i]+nums[j])
                left=j+1
                right=n-1
                while left<right:
                    if nums[left]+nums[right]>new_target:
                        right-=1
                    elif nums[right]+nums[left]<new_target:
                        left+=1
                    else:
                        x=(nums[i],nums[j],nums[left],nums[right])
                        if x not in dict_:
                            dict_.add(x)
                        left+=1
                        right-=1
        return [list(i) for i in dict_]
sol=Solution()
nums = [1,0,-1,0,-2,2]
target = 0
# nums = [2,2,2,2,2]
# target = 8
# nums=[0,0,0,0]
# target=0
print(sol.fourSum(nums,target))        