class Solution:
    def max_sum_i_s(self, arr, n):
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1, n):
            max_sum = 0
            for j in range(i - 1, -1, -1):
                if arr[i] > arr[j]:
                    max_sum = max(dp[j], max_sum)
            dp[i] = max_sum + arr[i]
        return dp[-1]

sol = Solution()
arr = [1, 101, 2, 3, 100]
arr = [1, 2, 3]
print(sol.max_sum_i_s(arr, len(arr)))
                
                    