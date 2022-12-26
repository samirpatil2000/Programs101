class Solution:
    
    def find_lower_elements(self, arr, value):
        start_index = 0
        end_index = len(arr) - 1
        while start_index <= end_index:
            mid_index = (start_index + end_index) // 2
            if arr[mid_index] <= value:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
            
        return start_index
    
sol = Solution()
arr = [1, 2, 6, 7, 9, 10]
value = 11
print(sol.find_lower_elements(arr, value))
import bisect
print(bisect.bisect(arr, value))