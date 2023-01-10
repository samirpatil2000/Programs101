class Solution:
    
    def get_element_count(self, arr:list, element: int):
        return arr.count(element)
    def majority_element(self, arr:list):
        element = arr[0]
        element_count = 1
        for i in range(1, len(arr)):
            print(i, arr[i], element, element_count)
            if arr[i] == element:
                element_count += 1
            else:
                element_count -= 1
            if element_count == 0:
                element = arr[i]
                element_count = 1
        if arr.count(element) > len(arr) // 2:
            return element
        return -1
   
arr = [3, 1, 3, 3, 2] 
arr = [1, 2, 3] 
print(Solution().majority_element(arr))
        