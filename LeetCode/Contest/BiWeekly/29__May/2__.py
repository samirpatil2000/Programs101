from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        result=0
        nums.sort()
        while i<j:
            result=max(result,nums[i]+nums[j])
            i+=1
            j-=1
        return result
    
    
sol=Solution()
nums =  [3,5,4,2,4,6]
print(sol.minPairSum(nums))