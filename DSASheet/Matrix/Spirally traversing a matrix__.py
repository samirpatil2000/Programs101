from typing import List


class Solution:
    def spiral_matrix(self, mat:List[List[int]]):
        direction = "right"
        top_wall = 0
        down_wall = len(mat) - 1
        left_wall = 0
        right_wall = len(mat[0]) - 1
        result = []
        while top_wall != down_wall or left_wall != right_wall:
            
            if direction == "right":
                row = top_wall
                for col in range(left_wall, right_wall + 1):
                    result.append(mat[row][col])
                top_wall += 1
                direction = "down"
                
            elif direction == "down":
                col = right_wall
                for row in range(top_wall, down_wall + 1):
                    result.append(mat[row][col])
                right_wall -= 1
                direction = "left"
            
            elif direction == "left":
                row = down_wall
                for row in range(right_wall, left_wall - 1, -1):
                    result.append(mat[row][col])
                down_wall -= 1
                direction = "top"
                
            else:
                col = left_wall
                for row in range(down_wall, top_wall - 1, -1):
                    result.append(mat[row][col])
                left_wall += 1
                direction = "right"
            
        return result
    

sol = Solution()
mat = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15,16]]
print(sol.spiral_matrix(mat))