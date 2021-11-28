# 53. Maximum Subarray



from typing import List


class Solution:
    def maxSubArrayUsingDivideAndConquer(self, nums: List[int],left:int,right:int) -> int:
        if left>right:
            return -2**32
        mid=(left+right)//2
        l_max=self.maxSubArrayUsingDivideAndConquer(nums,left,mid-1)
        r_max=self.maxSubArrayUsingDivideAndConquer(nums,mid+1,right)
        l_sum,l_max_sum=0,0
        for i in range(mid-1,left-1,-1):
            l_sum+=nums[i]
            l_max_sum=max(l_sum,l_max_sum)
        r_sum,r_max_sum=0,0   
        for i in range(mid+1,right+1):
            r_sum+=nums[i]
            r_max_sum=max(r_sum,r_max_sum)
        return max(l_max,r_max,l_max_sum+nums[mid]+r_max_sum)


            
        
            
sol=Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [-2,1]
print(sol.maxSubArrayUsingDivideAndConquer(nums,0,len(nums)-1))        