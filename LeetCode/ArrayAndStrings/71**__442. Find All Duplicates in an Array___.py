from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result_=[]
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0:
                result_.append(abs(nums[i]))
            nums[abs(nums[i])-1]*=-1
        return result_