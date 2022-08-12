class Solution:
    result = 0
    def explore_neighbor(self, mat, n, src_row, src_col, step, queue):
        dire = [[2, -1], [2, 1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
        for i in range(8):
            rr = src_row + dire[i][0]
            cc = src_col + dire[i][1]
            if rr < 0 or cc < 0:
                continue
            elif rr >= n or cc >= n:
                continue
            elif mat[rr][cc] == -1:
                continue
            queue.append([rr, cc, step + 1])
            
        
    def bfs(self, mat, n, knightPos, targetPos):
        import collections
        queue = collections.deque()
        queue.append([knightPos[0], knightPos[1], 0])
        while queue:
            node = queue.popleft()
            print(node)
            if mat[node[0]][node[1]] == -1:
                continue
            if node[0] == targetPos[0] and node[1] == targetPos[1]:
                return node[2]
            mat[node[0]][node[1]] = -1
            self.explore_neighbor(mat, n, node[0], node[1], node[2], queue)
        return -1
            
    def findPath(self, n, knightPos, targetPos):
        # code here
        n += 1
        mat = [[0] * n for _ in range(n)]
        print(mat)
        
        return self.bfs(mat, n, knightPos, targetPos)
    
    
sol = Solution()
N = 6
knightPos = [4, 5]
targetPos = [1, 1]

# N = 3
# knightPos = [3, 3]
# targetPos = [2, 1]
print(sol.findPath(N, knightPos, targetPos))