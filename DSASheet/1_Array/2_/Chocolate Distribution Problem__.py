class Solution:
    
    def findMinDiff(self, A, N,  M):
        
        A.sort()
        if M == len(A):
            return A[-1] - A[0]
        i = 0
        print(A)
        current_diff = A[-1] - A[0]
        while i + M - 1 < len(A):
            current_diff = min(current_diff, A[i + M - 1] - A[i])
            i += 1
        return current_diff
    
sol = Solution()
N = 7
M = 3
A = [7, 3, 2, 4, 9, 12, 56]
N = 8
M = 8
A = [3, 4, 1, 9, 56, 7, 12]
print(sol.findMinDiff(A, N, M))