class Solution:
    #Function to count subarrays with sum equal to 0.
    
    # this solution is not working 
    def dfs(self, arr, left, right):
        
        print( left, right)
        if left > right:
            return 0
        if left == right:
            return 1 if arr[left] == 0 else 0
        mid = (left + right) // 2
        total_counter = self.dfs(arr, left, mid - 1) + self.dfs(arr, mid + 1, right)
        print(left, right, mid)
        left_running_sum = 0
        for i in range(mid - 1, left - 1, -1):
            left_running_sum += arr[i]
        
        right_running_sum = 0   
        for i in range(mid + 1, right + 1):
            right_running_sum += arr[i]
            
        
        total_counter += ((left_running_sum + arr[mid]) == 0)
        total_counter += ((right_running_sum + arr[mid]) == 0) 
        total_counter += ((left_running_sum + right_running_sum + arr[mid]) == 0)
        
        print(total_counter, left_running_sum, right_running_sum)
        return total_counter
            
        
        
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        return self.dfs(arr, 0, n - 1)
arr = [0,0,5,5,0,0]
print(Solution().findSubArrays(arr, len(arr)))