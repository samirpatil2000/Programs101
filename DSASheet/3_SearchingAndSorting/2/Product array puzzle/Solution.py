class Solution:
    def productExceptSelf(self, arr, n):
        #code here
        arr_1 = [0] * n
        arr_2 = [0] * n
        arr_1[0] = arr_2[-1] = 1
        result = []
        print(arr_1, arr_2)
        for i in range(1, n):
            arr_1[i] = arr[i - 1] * arr_1[i - 1]
            last_index = n - i - 1
            arr_2[last_index] = arr_2[last_index + 1] * arr[last_index + 1]
            
        return [arr_1[i] * arr_2[i] for i in range(n)]
    
arr = [10, 3, 5, 6, 2]  
arr = [0, 19]  
print(Solution().productExceptSelf(arr, len(arr)))