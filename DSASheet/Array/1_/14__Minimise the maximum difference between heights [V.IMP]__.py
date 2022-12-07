from cgitb import small


class Solution:
    def getMinDiff(self, arr, k):
        arr.sort()
        
        result = arr[-1] - arr[0]
        small = arr[0] + k 
        large = arr[-1] - k
        
        for i in range(len(arr) - 1):
            
            min_ = min(arr[i + 1] - k, small)
            max_ = max(arr[i] + k, large)
            # if min_ < 0:
            #     continue
            result = min(result, max_ - min_)
            
        return result
    
sol = Solution()
arr = [3, 9, 12, 16, 20]
k = 3
arr = [2, 6, 3, 4, 7, 1, 2,10, 3, 2, 1]
k = 5

k = 5

arr = [8, 1 ,5 ,4 ,7 ,5 ,7 ,9 ,4 ,6]
print(sol.getMinDiff(arr, k))