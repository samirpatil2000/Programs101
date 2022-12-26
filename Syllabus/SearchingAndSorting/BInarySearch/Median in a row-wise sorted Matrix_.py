import bisect
class Solution:
    def brute_force(self, matrix):
        x = []
        [x.extend(matrix[i]) for i in range(len(matrix))]
        x.sort()
        middle_index = (len(matrix) * len(matrix[0]))// 2
        return x[middle_index]
        
        
    def find_greater_elements(self, matrix, value):
        result = 0
        for i in range(len(matrix)):
            result += bisect.bisect(matrix[i], value)
        return result
    
    def find_medium(self, matrix):
        start_value = 0
        end_value = 2000
        median_index = (len(matrix) * len(matrix[0]))// 2
        while start_value <= end_value:
            mid_value = (start_value + end_value) // 2
            result = self.find_greater_elements(matrix, mid_value)
            if result <= median_index:
                start_value = mid_value + 1
            else:
                end_value = mid_value - 1
        return start_value
    
sol = Solution()
matrix = [
    [1, 3, 5], 
    [2, 6, 9], 
    [3, 6, 9]
]
print(sol.find_medium(matrix))
print(sol.brute_force(matrix))