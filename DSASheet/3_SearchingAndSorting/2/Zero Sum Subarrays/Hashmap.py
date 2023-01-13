class Solution:
    #Function to count subarrays with sum equal to 0.
        
    def findSubArrays(self,arr,n):
        visited_sum = {0: 1}
        current_sum = 0
        result = 0
        for i in range(len(arr)):
            current_sum += arr[i]
            result += visited_sum.get(current_sum, 0)
            visited_sum[current_sum] = visited_sum.get(current_sum, 0) + 1
        return result
    

arr = [0,0,5,5,0,0] # 6
arr = [0,0,0] # 6
print(Solution().findSubArrays(arr, len(arr)))