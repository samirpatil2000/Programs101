import collections
from typing import List

class Solution:
    def bfs(self, mat, dp, c_row, c_col):
        queue = collections.deque()
        queue.append((c_row, c_col))
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            curr_row, curr_col = queue.popleft()
            for i in range(4):
                row = curr_row + DIR[i][0]
                col = curr_col + DIR[i][1]
                if row >= len(mat) or col >= len(mat[0]):
                    continue
                if row < 0 or col < 0:
                    continue
                if mat[row][col] == 'N':
                    dp[row][col] = 0
                    continue
                if mat[row][col] == 'W':
                    mat[row][col] = 'Visited'
                    dp[row][col] = 0
                    queue.append((row, col))
                elif mat[row][col] in ('H', '.'):
                    if dp[row][col] == -1 or dp[row][col] > (dp[curr_row][curr_col] + 2):
                        dp[row][col] = dp[curr_row][curr_col] + 2
                        queue.append((row, col))
                
            
    def chefAndWells(self, n : int, m : int, mat : List[List[str]]) -> List[List[int]]:
        dp = [[-1] * len(mat[0]) for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 'W':
                    dp[row][col] = 0
                    self.bfs(mat, dp, row, col)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == '.':
                    dp[row][col] = 0
        return dp

sol = Solution()
n, m = 4, 5

mat = [
[ '.', '.', 'W', '.', 'W'],
['N', 'W', 'N', 'N', 'W'],
['H', '.', '.', 'H', 'N'],
['N', 'N', 'N', '.', 'W']]

# n = 3
# m = 3
# mat = [
# ['H', 'H', 'H'],
# ['H', 'W', 'H'],
# ['H', 'H', '.'],]


# n = 5
# m = 5
# mat = [

# ['H', 'N', 'H', 'H', 'H'],
# ['N', 'N', 'H', 'H', 'W'],
# ['W', 'H', 'H', 'H', 'H'],
# ['H', 'H', 'H', 'H', 'H'],
# ['H', 'H', 'H', 'H', 'H']
# ]

print(sol.chefAndWells(n, m, mat))