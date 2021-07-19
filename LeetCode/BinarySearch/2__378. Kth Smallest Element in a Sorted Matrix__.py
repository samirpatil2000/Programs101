from typing import List
import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left=matrix[0][0]
        right=matrix[-1][-1]
        while left<right:
            mid=(left+right)//2
            
            sum_=sum(bisect.bisect(row,mid) for row in matrix)
            if sum_<k:
                left=mid+1
            else:
                right=mid
        return left
    
sol=Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(sol.kthSmallest(matrix,4))
            
                 
            
            