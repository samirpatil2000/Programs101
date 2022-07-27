class Solution:
    def separate(self, arr):
        start, end = 0, len(arr) - 1
        while start < end:
    
            if arr[start] >= 0:
                start += 1
            if arr[end] < 0:
                end -= 1
 
            if arr[start] < 0 and arr[end] >= 0:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

    def find_first_negative(self, arr):
        for i in range(len(arr)):
            if arr[i] < 0:
                return i
        return -1
                
    def rearrange(self, arr):
        self.separate(arr)
        i, j = 0, self.find_first_negative(arr)
        while i < j and j < len(arr):
            if i & 1 == 0:
                # even
                i += 1
                continue
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        return arr
    
sol = Solution()
arr = [1, 2, 3, -4, -1, 4]
arr = [-7, -1, 8]
# arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(sol.rearrange(arr))
            
            
        