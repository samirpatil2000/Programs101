from collections import defaultdict
class Solution:
    largest_cycle_length = 0
    def create_graph(self, edges):
        graph = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                graph[i].append(edges[i])
        return graph
    
    def find_max_weight_node(self, edges):
        max_weight = -1
        max_node = -1
        weights = [0] * len(edges)

        for i in range(len(edges)):
            if edges[i] != -1:
                weights[edges[i]] += 1
        
        for i in range(len(edges)):
            if weights[i] > max_weight:
                max_weight = weights[i]
                max_node = i
        return max_node

    def dfs(self, graph, node, start_node, cycle_length, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if neighbor == start_node:
                self.largest_cycle_length = max(self.largest_cycle_length, cycle_length + 1)
            elif not visited[neighbor]:
                self.dfs(graph, neighbor, start_node, cycle_length + 1, visited)

        visited[node] = False  # backtrack
    
    def find_largest_cycle_length(self, edges):
        graph = self.create_graph(edges)
        visited = [False] * len(edges)

        for i in range(len(edges)):
            self.dfs(graph, i, i, 0, visited)

        return self.largest_cycle_length
    

# t = int(input())
# while t:
#     t -= 1
#     edges = [int(i) for i in input().strip().split()]
#     print(Solution().find_max_weight_node(edges))
    
edges = [1, 2, 3, 4, 0]
edges = [1, 2, -1, 4, 5, -1, -1]
edges =  [1, 2, 3, -1, 5, 6, 0, 7, 8]
print(Solution().find_largest_cycle_length(edges))
            
    
    