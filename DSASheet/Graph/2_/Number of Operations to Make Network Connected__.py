from typing import List


class Solution:
    def dfs(self, graph, src, visited):
        visited.add(src)
        for edge in graph[src]:
            if edge in visited:
                continue
            self.dfs(graph, edge, visited)
            
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        if len(connections) < 6:
            return -1
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        componet = 0
        for src in graph:
            if src in visited:
                continue
            componet += 1
            self.dfs(graph, src, visited)
        return componet - 1

sol = Solution()
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
n = 4
connections = [[0,1],[0,2],[1,2]]
n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]
print(sol.makeConnected(n, connections))
        
        