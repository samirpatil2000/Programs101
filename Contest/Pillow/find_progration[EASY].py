class Solution:
    
    def is_arithmentic_progration(self, arr):
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i] + diff != arr[i + 1]:
                return False
        return True
    
    def is_geometric_progration(self, arr):
        ratio = arr[1] // arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] // arr[i] != ratio:
                return False
        return True
    
    def find_progration(self, arr):
        if len(arr) < 2:
            return "-1"
        if self.is_arithmentic_progration(arr):
            return "Arithmetic"
        if self.is_geometric_progration(arr):
            return "Geometric"
        return "-1"
            
arr = [2, 4, 6, 8]
arr = [2, 6, 18, 54]
print(Solution().find_progration(arr))