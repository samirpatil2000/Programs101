
class Solution:
    def rearrange(self, arr):
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] <= 0:
                left += 1
            if arr[right] > 0:
                right -= 1
            if arr[left] > 0 and arr[right] <= 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            print(arr)
                            
sol = Solution()  
arr = [0, 3, -2, 1, 2, -3]  
sol.rearrange(arr)
print(arr)



def