class Solution:
    
    
    def is_valid(self, matrix, row, col):
        if row < 0 or col < 0:
            return False
        if row >= len(matrix) or col >= len(matrix[0]):
            return False
        if matrix[row][col] == "#":
            return False
        return True
    
    def dfs(self, matrix, row, col, index, word):
        if matrix[row][col] != word[index]:
            return False
        if len(word) - 1 == index:
            return True
        matrix[row][col] = "#"
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for i in range(8):
            new_row, new_col = directions[i][0] + row, directions[i][1] + col
            if (self.is_valid(matrix, new_row, new_col) and 
                    self.dfs(matrix, new_row, new_col, index + 1, word)):
                    matrix[row][col] = word[index]
                    return True
        matrix[row][col] = word[index]
        return False 
    
    def find_word(self, string_array):
        result = []
        matrix = [list(word) for word in string_array[0].split(", ")]
        for word in string_array[1].split(","):
            if not self.find_word_in_matrix(matrix, word):
                result.append(word)
        return str(result)[1:-1] if len(result) else True
        
    def find_word_in_matrix(self, matrix, word):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if self.dfs(matrix, row, col, 0, word):
                    return True
        return False
    
    
Input = ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]
Output = "true"

Input = ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]
Output = "rumk,yes"
[
    ['a', 'a', 'e', 'y'], 
    ['r', 'r', 'u', 'm'], 
    ['t', 'g', 'm', 'n'], 
    ['b', 'a', 'l', 'l']
]
print(Solution().find_word(Input))


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
arr = [5, 10, 15]
print(Solution().find_progration(arr))