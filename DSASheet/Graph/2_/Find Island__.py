import imp


import collections
class Solution:
    def dfs(self, mat, src_row, src_col):
        mat[src_row][src_col] = -1
        dr = [+1, +1, +1, -1, -1, -1, 0, 0]
        dc = [ 0, +1, -1, 0, +1, -1, +1, -1]
        for i in range(8):
            row, col = src_row + dr[i], src_col + dc[i]
            if row < 0 or col < 0:
                continue
            if row >= len(mat) or col >= len(mat[0]):
                continue
            if mat[row][col] == -1 or mat[row][col] == 0:
                continue
            self.dfs(mat, row, col)
            
    def bfs(self, mat, src_row, src_col):
        mat[src_row][src_col] = -1
        queue = collections.deque()
        queue.append([src_row, src_col])
        while queue:
            temp = queue.popleft()
            dr = [+1, +1, +1, -1, -1, -1, 0, 0]
            dc = [ 0, +1, -1, 0, +1, -1, +1, -1]
            for i in range(8):
                row, col = temp[0] + dr[i], temp[1] + dc[i]
                if row < 0 or col < 0:
                    continue
                elif row >= len(mat) or col >= len(mat[0]):
                    continue
                elif mat[row][col] == -1 or mat[row][col] == 0:
                    continue
                mat[row][col] = -1
                queue.append([row, col])        
            
    def numIslands(self, grid):
        #code here
        island = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == -1 or grid[row][col] == 0:
                    continue
                island += 1
                self.bfs(grid, row, col)
        return island
    
sol = Solution()
n, m = map(int, input().strip().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input().strip().split())))
print(sol.numIslands(grid))