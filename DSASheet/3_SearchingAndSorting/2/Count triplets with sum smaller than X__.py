class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort()
        result = 0
        for i in range(n):
            start = i + 1
            end = n - 1
            
            while start < end:
                current_sum = arr[start] + arr[end] + arr[i]
                print(arr[start] + arr[end] + arr[i], arr[start] , arr[end] , arr[i])
                if current_sum < sumo:
                    start += (end - start)
                    result += 1
                else:
                    end -= 1
        return result

arr = [-2, 0, 1, 3]
k = 2
print(Solution().countTriplets(arr, len(arr), k))