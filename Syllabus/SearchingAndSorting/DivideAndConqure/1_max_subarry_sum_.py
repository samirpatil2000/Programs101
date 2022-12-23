from typing import List


class Solution:
    
    def max_subarray_sum(self, arr:List[int], left, right):
        
        if left > right:
            return -2 ** 32 # max_sum, current_sum
        
        mid = (left + right) // 2
        
        left_max = self.max_subarray_sum(arr, left, mid - 1) 
        right_max = self.max_subarray_sum(arr, mid + 1, right)
        
        l_sum, l_sum_max = 0, 0
        for i in range(mid - 1, left + 1, -1):
            l_sum += arr[i]
            l_sum_max = max(l_sum_max, l_sum)
            
        r_sum, r_sum_max = 0, 0
        for i in range(mid + 1, right + 1):
            r_sum += arr[i]
            r_sum_max = max(r_sum_max, r_sum)
           
        return max(l_sum_max + arr[mid] + r_sum_max, left_max, right_max)

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
# nums = [-2,1]
left, right = 0, len(nums) - 1
print(sol.max_subarray_sum(nums, left, right))