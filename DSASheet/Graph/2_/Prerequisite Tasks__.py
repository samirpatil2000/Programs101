import collections

class Solution:
    
    def isPossible(self, vertices, prerequisites):
        graph = {i: [] for i in range(vertices)}
        for u, v in prerequisites:
            graph[u].append(v)
        indegrees = [0] * vertices
        
        count_node = 0
        for src in graph:
            for edge in graph[src]:
                indegrees[edge] += 1
        
        queue = collections.deque()
        
        for i in range(vertices):
            if indegrees[i] == 0:
                queue.append(i)
                count_node += 1
                
        while queue:
            node = queue.popleft()
            for edge in graph[node]:
                indegrees[edge] -= 1
                if indegrees[edge] == 0:
                   queue.append(edge)
                   count_node += 1
        return count_node == vertices
                    
                    
sol = Solution()
vertices = 10
list_ = [(1, 3), (1, 4), (1, 5), (2, 3), 
         (2, 8), (2, 9), (3, 6), (4, 6), 
         (4, 8), (5, 8), (6, 7), (7, 8), (8, 10)]
N = 4
prerequisites =  [[1, 0],
                  [2, 1], 
                  [3, 2]] 

N = 2
prerequisites =  [ [1,0] , [0,1] ] 

print(sol.isPossible(N, prerequisites))


        