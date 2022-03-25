from typing import List


class Solution:
    def findMin(self, arr: List[int]):
        dp = [1] * len(arr)
        dp[-1] = 0
        for i in range(len(dp) - 2, -1, -1):
            if i + arr[i] >= len(arr):
                dp[i] = 1
            else:
                min_ = 2 ** 32
                for j in range(1, arr[i] + 1):
                    min_ = min(min_, dp[i + j])
                dp[i] = min_ + 1
        print(dp)
        return dp[0]
    
    
sol = Solution()
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr = [1, 4, 3, 2, 6, 7]
print(sol.findMin(arr))