import collections
class Solution:
    
    #Function to detect cycle in a directed graph.
    def toposort_using_bfs(self, graph, vertices):
        indegrees = [0] * vertices
        print(vertices)
        for src in range(vertices):
            for edge in graph[src]:
                indegrees[edge] += 1
        queue = collections.deque()
        for i in range(vertices):
            if indegrees[i] == 0 :
                queue.append(i)
        free_node = 1
        while queue:
            src = queue.popleft()
            for edge in graph[src]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                    free_node += 1
                    queue.append(edge)
        if free_node == vertices:
            return False
        return True
        
        
    def isCyclic(self, V, adj):
        # code here
        graph = collections.defaultdict(list)
        for u, v in adj:
            graph[u].append(v)
        return self.toposort_using_bfs(graph, V)
    
sol = Solution()
V = 6
adj = [[5, 3], [3, 1], [1, 2], [2, 4], [4, 0]]
print(sol.isCyclic(V, adj))