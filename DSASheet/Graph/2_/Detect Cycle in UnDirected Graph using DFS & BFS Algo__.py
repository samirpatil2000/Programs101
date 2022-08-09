class Solution:
    
    #Function to detect cycle in an undirected graph.
    def detect_cycle(self, vertices, graph):
        visited = set()
        for src in range(vertices):
            if src in visited:
                continue
            # if self.dfs(graph, src, visited):
            if self.bfs(graph, src, visited):
                return True
        return False
            
    def dfs(self, graph, src, visited, parent=None):
        visited.add(src)
        for edge in graph[src]:
            if edge not in visited:
                if self.dfs(graph, edge, visited, parent=src):
                    return True
            elif parent != edge:
                return True
        return False
    
    def bfs(self, graph, src, visited):
        import collections
        queue = collections.deque()
        queue.append(src)
        while queue:
            src = queue.popleft()
            if src in visited:
                return True
            visited.add(src)
            for edge in graph[src]:
                if edge in visited:
                    continue
                queue.append(edge)
        return False
        
    def isCycle(self, V, adj):
	    return self.detect_cycle(V, adj)
 
 
sol = Solution()
V = 5
adj =  [[1],  [0, 2, 4],  [1, 3],  [2, 4],  [1, 3]]  

# V = 4
# adj = [[], [2], [1, 3], [2]] 
print(sol.isCycle(V, adj))