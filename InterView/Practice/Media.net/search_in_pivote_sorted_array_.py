class Solution:
    
    def search_in_arr(self, arr, left, right, target):
        
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > arr[left]:
            if arr[left] <= target and arr[mid] > target:
                return self.search_in_arr(arr, left, mid - 1, target)
            return self.search_in_arr(arr, mid + 1, right,  target)
        else: # arr[-1] > arr[mid]
            if arr[right] >= target and arr[mid] < target:
                return self.search_in_arr(arr, mid + 1, right, target)
            return self.search_in_arr(arr, left, mid - 1, target)
        
        
                
    def find_element(self, arr, target):
        return self.search_in_arr(arr, 0, len(arr) - 1, target)
    

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3] 
target = 10
print(Solution().find_element(arr, target))