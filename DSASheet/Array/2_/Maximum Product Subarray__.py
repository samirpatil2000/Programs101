#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
    def maxProduct(self,arr):
        max_ = arr[0]
        min_ = arr[0]
        result = arr[0]
        for i in range(1, len(arr)):
            temp = min_
            min_ = min(arr[i], min_ * arr[i], max_ * arr[i])
            max_ = max(arr[i], max_ * arr[i], temp * arr[i])                        
            result = max(max_, result)
        return result
        
  
       
sol = Solution()
arr = [6, -3, -10, 0, 2]
arr = [-8 ,5 ,3 ,1 ,6]
# arr = [9, 0, 8, -1, -2, -2, 6]
print(sol.maxProduct(arr))


x = [[2, 3], [4, 5]]

