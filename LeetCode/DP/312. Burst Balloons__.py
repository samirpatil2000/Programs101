from typing import List


class Solution:
    count_=0
    def product(self,index:int,nums:List[int]):
        left,right=1,1
        if index<len(nums)-1:
            right=nums[index+1]
        if index>0:
            left=nums[index-1]
        return right*nums[index]*left
    def maxCoins(self, nums: List[int],memo={}) -> int:
        max_=0
        if nums in memo:
            return memo[nums]
        for i in range(len(nums)):
            prod=self.product(i,nums)
            print(nums,i,nums[i],"prod="+str(prod))
            self.count_+=1
            max_=max(self.maxCoins(nums[:i]+nums[i+1:],memo=memo)+prod,max_)
        memo[nums]=max_
        return max_

sol=Solution()
nums=(3,1,5,8)
memo={}
print(sol.maxCoins(nums,memo))
print(sol.count_)
print(memo)