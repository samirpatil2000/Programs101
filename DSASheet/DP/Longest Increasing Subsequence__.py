class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        dp = [0] * n
        result = 0
        dp[0] = 1
        for i in range(1, n):
            max_ = 0
            for j in range(i, -1, -1):
                if a[i] > a[j]:
                    max_ = max(max_, dp[j])
            dp[i] = max_ + 1
            result = max(result, dp[i])
        return result
    
    def longestSubsequence_NLOGN(self, a, n):
        import bisect
        
        dp = [2 ** 32] * (n + 1)
        dp[0] *= -1
        
        for i in range(n):
            index = bisect.bisect(dp, a[i])
            if dp[index - 1] < a[i] and dp[index] > a[i]:
                dp[index] = a[i]
        for i in range(n, -1, -1):
            if dp[i] != 2 ** 32:
                return i
        return 0
    
sol = Solution()
N = 16
A = [0,8,4,12,2,10,6,14,1,9,5, 13,3,11,7,15]
N = 6
A = [5,8,3,7,9,1]
N = 3
A = 1, 3, 7
print(sol.longestSubsequence(A, N))
print(sol.longestSubsequence_NLOGN(A, N))
            
        