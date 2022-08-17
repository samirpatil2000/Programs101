class Solution:
    
    def toposort(self, list_, vertices):
        graph = {i: [] for i in range(vertices)}

        for u, v in list_:
            graph[u - 1].append(v - 1)
        indegrees = [0] * vertices
        import collections
        for src in graph:
            for edge in graph[src]:
                indegrees[edge] += 1
        
        queue = collections.deque()
        for i in range(vertices):
            if indegrees[i] == 0:
                queue.append([i, 1])
        result = [0] * vertices
        while queue:
            node, state = queue.popleft()
            result[node] = state
            result
            for edge in graph[node]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                   queue.append([edge, state + 1])
        return result
                    
                    
sol = Solution()
vertices = 10
list_ = [(1, 3), (1, 4), (1, 5), (2, 3), 
         (2, 8), (2, 9), (3, 6), (4, 6), 
         (4, 8), (5, 8), (6, 7), (7, 8), (8, 10)]

print(sol.toposort(list_, vertices))

        