class Solution:
    
    def get_min_max(self, arr: list, left: int, right: int):
        if left > right:
            return -1, 2 ** 32
        if left == right:
            return arr[left], arr[right]
        elif left + 1 == right:
            return max(arr[left], arr[right]), min(arr[left], arr[right])
        else:
            mid = (left + right) // 2
            left_max, left_min = self.get_min_max(arr, left, mid - 1)
            right_max, right_min = self.get_min_max(arr, mid + 1, right)
            return max(left_max, right_max, arr[mid]), min(left_min, right_min, arr[mid])
        

arr = [1000, 11, 445, 1, 330, 3000]
arr = [1]
print(Solution().get_min_max(arr, 0, len(arr) - 1))