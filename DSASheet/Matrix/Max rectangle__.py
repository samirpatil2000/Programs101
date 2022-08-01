import re


class Solution:
    
    
    def find_left_min(self, arr):
        left_min = []
        st = [-1]
        for i in range(len(arr)):
            while st[-1] != -1 and arr[i] <= arr[st[-1]]:
                st.pop()
            left_min.append(st[-1])
            st.append(i)
        return left_min
    
    def find_right_min(self, arr, left_min):
        n = len(arr)
        st = [n]
        result = 0
        for i in range(n - 1, -1, -1):
            while st[-1] != n and arr[i] <= arr[st[-1]]:
                st.pop()
            result = max(result, (st[-1] - left_min[i] - 1) * arr[i])
            st.append(i)
        return result
            
    def largetArea(self, arr):
        left_min = self.find_left_min(arr)
        result = self.find_right_min(arr, left_min)
        return result
    
    
    def maxArea(self, M, n, m):
        hist = M[0]
        result = self.largetArea(hist)
        for i in range(1, n):
            for j in range(m):
                hist[j] += 1 
                hist[j] *= M[i][j]
            result = max(self.largetArea(hist), result)
        return result
                

sol = Solution()
mat = [ [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0] ]
# mat = [[1, 1, 1, 1, 1],
# [0, 1, 0, 0, 0]]
mat = [[7, 2, 8, 9, 1, 3, 6, 5]]
print(sol.maxArea(mat, len(mat), len(mat[0])))