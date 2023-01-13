class Solution:
    
    def merge(self, arr1, arr2, n, m):
        for i in range(m):
            extra_element = self.insert_in_arr_1(self, arr1, arr2[i])
            self.insert_in_arr_2(self, arr2, extra_element)
        
    def insert_in_arr_1(self, arr, element):
        if element >= arr[-1]:
            return element
        i = len(arr) - 2
        last_element = arr[i]
        while i >= 0 and arr[i] <= element:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = element
        return last_element 
    
    def insert_in_arr_2(self, arr, element): 
        i = len(arr) - 2
        last_element = arr[-1]
        while i >= 0 and arr[i] <= element:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = element
        return
        
            