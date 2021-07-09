from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ROW=len(nums1)+1
        COL=len(nums2)+1
        dp=[[0]*COL for _ in range(ROW)]
        max_=0
        for row in range(ROW):
            for col in range(COL):
                if row==0 or col==0:
                    continue
                if nums1[row-1]==nums2[col-1]:
                    dp[row][col]=1+dp[row-1][col-1]
                
                    max_=max(dp[row][col],max_)
        return max_
    
sol=Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
nums1 = [0,0,0,0,0]
nums2 = [0,0,0,0,0]
print(sol.findLength(nums1,nums2))