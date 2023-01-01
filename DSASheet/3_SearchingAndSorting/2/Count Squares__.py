
import math

from icecream import ic

class Solution:
    
    def countSquares(self, N):
        # code here 
        ans = 1
        for i in range(2, int(math.sqrt(N)) + 1):
            if i * i >= N:
                return ans
            ans = i
        return ans
    
    def with_binary_search(self, N):
        
        left = 0
        right = int(math.sqrt(N))
        while left < right:
            mid = (left + right) // 2
            if mid * mid < N:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
        
            



N = 81
ic(Solution().countSquares(N))
ic(Solution().with_binary_search(N))