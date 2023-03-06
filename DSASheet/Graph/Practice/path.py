from typing import Dict, List
from collections import defaultdict, deque

class Solution:
    
    def create_graph(self, nodes: List[List[int]]):
        graph = defaultdict(list)
        for i in range(len(nodes)):
            u, v = nodes[i]
            graph[u].append(v)
            graph[v].append(u)
        return graph
        
    def dfs(self, graph: Dict, src: str, end: str, visited=set()):
        if src == end: return True
        if src in visited: return False
        visited.add(src)
        for edge in graph[src]:
            if edge in visited: continue
            if self.dfs(graph, edge, end, visited): return True        
        return False
    
    def bfs(self, graph: Dict, src: str, end: str):
        queue = deque()
        queue.append(src)
        visited = set()
        while queue:
            src = queue.popleft()
            if src == end: return True
            if src in visited: 
                continue
            visited.add(src)
            for edge in graph[src]:
                if edge in visited: continue
                queue.append(edge)
        return False
                
        
    
    def find_path(self, nodes: List[List[int]], src: int, end: int):
        graph = self.create_graph(nodes)
        result = []
        result.append(self.dfs(graph, src, end))
        result.append(self.bfs(graph, src, end))
        return result
    
nodes = [[1, 2], [1, 4], [4, 3], [3, 2]]
nodes = [[0, 1], [0, 2], [1, 2], [3, 2], [3, 3], [4, 5]]
U, V = 5, 5
print(Solution().find_path(nodes, U, V))
            
             
        