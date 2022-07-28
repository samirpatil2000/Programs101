
class Solution:
    
    def minSwap (self, arr, n, k) : 
        
        non_favorable = 0
        window_size = 0
        for i in range(n):
            if arr[i] <= k:
                window_size += 1

        for i in range(window_size):
            if arr[i] > k:
                non_favorable += 1
        print(window_size, non_favorable)
        result = non_favorable
            
        for i in range(n - window_size):
            print(result, arr[i], arr[i + window_size])
            if arr[i] > k:
                non_favorable -= 1
            if arr[i + window_size] > k:
                non_favorable += 1
            
            result = min(non_favorable, result)
        return result

sol = Solution()
arr = [2, 1, 5, 6, 3]
k = 3
arr = [2, 7, 9, 5, 8, 7, 4]
k = 6
print(sol.minSwap(arr, len(arr), k))
            