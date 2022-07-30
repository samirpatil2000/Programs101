class Solution:
    
    def rowWithMax1s(self,arr):
     
		# code here
        col = len(arr[0]) - 1
        row = 0
        result = 1e4
        while col >= 0 and row < len(arr):

            if arr[row][col] == 1:
                result = min(result, col)
                col -= 1
            else:
                row += 1
        if result == 1e4:
            return 0
        return len(arr[0]) - result
 
sol = Solution()
arr = []
print(sol.rowWithMax1s(arr))