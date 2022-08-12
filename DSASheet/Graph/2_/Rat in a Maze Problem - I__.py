class Solution:
    result = set()
    def explore_neighbor(self, mat, n, src_row, src_col, path):
        dire = [[1, 0, "D"], [-1, 0, "U"], [0, 1, "R"], [0, -1, "L"]]
        for i in range(4):
            rr = src_row + dire[i][0]
            cc = src_col + dire[i][1]
            if rr < 0 or cc < 0:
                continue
            elif rr >= n or cc >= n:
                continue
            elif mat[rr][cc] == -1 or mat[rr][cc] == 0:
                continue
            self.dfs(mat, n, rr, cc, path + dire[i][2])
    
            
    def dfs(self, mat, n, src_row, src_col, path = ""):
        if src_row == n - 1 and src_col == n - 1:
            self.result.add(path)
            return
        temp = mat[src_row][src_col]
        mat[src_row][src_col] = -1
        self.explore_neighbor(mat, n, src_row, src_col, path)
        mat[src_row][src_col] = temp
        
    def findPath(self, mat, n):
        # code here
        if mat[0][0] == 0:
            return []
        self.dfs(mat, n, 0, 0)
        return list(self.result) if self.result else []
        
            

sol = Solution()
mat = [ [ 1, 0, 0, 0] ,
        [ 1, 1, 0, 1] , 
        [ 1, 1, 0, 0] ,
        [ 0, 1, 1, 1] ] 

mat = [[1, 0], [1, 0]]
# mat = [[1, 0, 1, 0]]

mat = [[0, 1, 1, 1],
       [1, 1, 1, 0], 
       [1, 0, 1, 1], 
       [0, 0, 1, 1]]

print(sol.findPath(mat, len(mat)))
            
            
            