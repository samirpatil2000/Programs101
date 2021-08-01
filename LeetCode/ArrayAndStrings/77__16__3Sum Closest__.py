from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=nums[0]+nums[1]+nums[2]
        
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if abs(sum-target)<abs(closest_sum-target):
                    closest_sum=sum
                if sum==target:
                    return target
                elif sum<target:
                    j+=1
                else:
                    k-=1
        return closest_sum
                
sol=Solution()
nums = [-1,2,1,-4]
target = 1

print(sol.threeSumClosest(nums,target))