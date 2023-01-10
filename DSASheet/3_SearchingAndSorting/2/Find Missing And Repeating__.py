
class Solution:
    def findTwoElement(self, arr, n): 
        # code here
        result = []
        for i in range(len(arr)):
            next_element = arr[abs(arr[i]) - 1]
            if next_element < 0:
                result.append(abs(arr[i]))
            if arr[abs(arr[i]) - 1] > 0:
                
                arr[abs(arr[i]) - 1] = arr[abs(arr[i]) - 1] * -1 
        
        print(arr)
        for i in range(len(arr)):
            if arr[i] > 0:
                result.append(i + 1)
                return result
           
arr = [2, 1, 5, 3, 3] 
arr = [2, 1, 6, 3, 4, 6] 
arr = [3, 7, 6, 2, 5, 6, 1] 
arr = [13, 33, 43, 16, 25, 19, 23, 31, 29, 35, 10, 2, 32, 11, 47, 15, 34, 46, 30, 26, 41, 18, 5, 17, 37, 39, 6, 4, 20, 27, 9, 3, 8, 40, 24, 44, 14, 36, 7, 38, 12, 1, 42, 12, 28, 22, 45]
print(Solution().findTwoElement(arr, 0))