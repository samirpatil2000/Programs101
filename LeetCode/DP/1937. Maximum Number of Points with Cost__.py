from typing import List


class Solution:
    def maxPoints(self, mat: List[List[int]]) -> int:
        dp=mat[0].copy()
        for row in range(1,len(mat)):
            temp=dp.copy()
            for col in range(len(mat[0])):
                max_=-1
                for i in range(len(mat[0])):
                    max_=max(max_,mat[row][col]+dp[i]-abs(col-i))
                temp[col]=max_
            dp=temp
        return max(dp)

sol=Solution()
mat=[[1,2,3],[1,5,1],[3,1,1]]
mat=[[1,5],[2,3],[4,2]]
print(sol.maxPoints(mat[:1]))