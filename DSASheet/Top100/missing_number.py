
class Solution:
    def missingNumber(self, arr, n):
        # code here
        for i in range(n):
            next_index = abs(arr[i]) - 1
            print(next_index, n)
            if next_index >= n:
                continue
            arr[next_index] *= -1
            
        for i in range(n):
            if arr[i] >= 0:
                return i + 1
            
arr = []
print(Solution().missingNumber(arr, len(arr)))