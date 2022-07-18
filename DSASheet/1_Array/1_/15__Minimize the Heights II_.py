#User function Template for python3

class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        result = arr[-1] - arr[0]
        small = arr[0] + k
        large = arr[-1] - k
        print(arr)
        print(small, large)
        for i in range(len(arr) - 1):
            print("i-", i , arr[i], arr[i + 1])
            if arr[i + 1] < k:
                continue
            
            min_ = min(small, arr[i + 1] - k)
            max_ = max(large, arr[i] + k)
            result = min(result, max_ - min_)
            print("-i",min_, max_, result)
        return result
    
sol = Solution()
arr = [1, 2, 2, 2, 3, 4, 6, 7, 10]
k = 5
print(sol.getMinDiff(arr, k))