class Solution:
    
    def change_arr(self, array):
        for i in range(len(array)):
            for j in range(1 + i, len(array)):
                if array[j] + array[i] > array[i] + array[j]:
                    array[i], array[j] = array[j], array[i] 
        print(array)
    
    def largest_number_value(self, arr):
        # arr = 
        arr.sort(key=lambda x: str(x), reverse=True)
        return "".join(map(lambda x: str(x), arr))

sol = Solution()
arr = [1, 34, 3, 98, 9, 76, 45, 4]
# arr = [54, 546, 548, 60]
print(sol.largest_number_value(arr))
sol.change_arr(arr)