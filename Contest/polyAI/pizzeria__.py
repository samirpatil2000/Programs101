from typing import List, Set


class Solution:
    def bfs(self, mat: List[List[int]], row: int, col: int, round_: int, visited: Set):
        queue = [(row, col, round_)]
        max_ = 0
        while queue:
            x, y, r = queue.pop(0)
            position = str(x) + "-" + str(y)
            if x >= len(mat) or y >= len(mat[0]) or x < 0 or y < 0:
                continue
            if position in visited or r == 0:
                continue
            mat[x][y]+=1
            max_ = max(mat[x][y], max_)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add(position)
            for u, v in directions:
                queue.append((x + u, y + v, r - 1))
        return max_
                    
    def pizz(self):
        
        # n, t = [int(i) for i in input().split()]
        # mat = [[0]*n for _ in range(n)]
        # ans = 0
        # for _ in range(t):
        #     row, col, round_ = [int(i) for i in input().split()]
        #     visited = set()
        #     ans = max(ans, self.bfs(mat, row - 1, col - 1, round_ + 1, visited))
        # return ans,mat
        
        n, t = (5, 2)
        mat = [[0] * n for _ in range(n)]
        ans = 0
        qu = [(3, 3, 2), (1 , 1, 2)]
        for row, col,round_ in qu:
            visited = set()
            ans = max(ans, self.bfs(mat, row - 1, col - 1, round_ + 1, visited))
        for q in mat:
            print(q)
        return ans
    
"""
5 2 
3 3 2 
1 1 2
"""

sol = Solution()
print(sol.pizz())