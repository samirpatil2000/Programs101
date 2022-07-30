class Solution:
    def sort(self, arr):
        if len(arr) > 2:
            temp = arr[0]
            i = 1
            while i < len(arr) and temp > arr[i]:
                arr[i - 1] = arr[i]
                i += 1
            arr[i - 1] = temp
        else:
            arr.sort()
        return arr
            
    def insert(self, arr1, arr2):
        last = arr1[-1]
        i = len(arr1) - 2
        while i >= 0 and arr2[0] <= arr1[i]:
            arr1[i + 1] = arr1[i]
            i -= 1
        arr1[i + 1] = arr2[0]
        arr2[0] = last
        
    
    def merge(self, arr1, arr2, n=0, m=0):
        while arr2[0] < arr1[-1]:
            self.insert(arr1, arr2)
            self.sort(arr2)
        return arr1 , ",", arr2



sol = Solution()
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

# arr1 = [12, 45, 57]
# arr2 = [20]
print(sol.merge(arr1, arr2))

            
