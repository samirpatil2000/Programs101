import collections
class Solution:
    
    
    def create_graph(self, edges, nodes):
        graph = {i + 1:set() for i in range(nodes)}
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return graph
    
    # def remove_node(self, src, w):
        
    def dfs(self, graph, src, visited, weights):
        visited.add(src)
        nodes_to_remove = []
        for e in graph[src]:
            if e in visited:
                continue
            res = self.dfs(graph, e, visited, weights)
            if not res:
                nodes_to_remove.append(e)
        for node in nodes_to_remove:
            graph[src].remove(node)
            graph[node].remove(src)

        if weights[src - 1] & 1 == 0 and len(graph[src]) == 1:
            return False
        return True
    
    def remove_nodes(self, edges, weights, nodes):
        graph = self.create_graph(edges, nodes)
        print(graph)
        self.dfs(graph, 1, set(), weights)
        print(graph)
             
             
             

        
    
nodes = 10
edges = [[1, 3], [2, 10], [3, 9], [4, 5], [5, 2], [6, 3], [7, 3], [8, 3], [9, 4]]

weights = [78, 61, 91, 63, 9, 68, 23, 45, 96, 66] 

nodes = 6
edges = [[1, 2], [2, 3], [3, 6], [4, 2], [5, 1]]

weights = [78, 60, 90, 62, 9, 68] 
sol = Solution()
print(sol.remove_nodes(edges, weights, nodes))
# print(sol.)


















    
# T = int(input())
# test_ = T
# inputs_ = []

# while T:
#     T -= 1
#     e = int(input()) - 1
#     edges = []
#     while e:
#         e -= 1
#         edges.append([int(i) for i in input().strip().split()])
#     weights = [int(i) for i in input().strip().split()]
#     inputs_.append([edges, weights])
#     ans = []
# while test_:
#     test_ -= 1
#     ans.append([int(i) for i in input().strip().split()])

# print(inputs_)
# print(ans)




[[[[1, 3], [2, 10], [3, 9], [4, 5], [5, 2], [6, 3], [7, 3], [8, 3], [9, 4]], 
    [78, 61, 91, 63, 9, 68, 23, 45, 96, 66]], 
 [[[1, 7], [2, 8], [3, 7], [4, 8], [5, 1], [6, 3], [7, 4]], 
    [73, 93, 100, 19, 17, 86, 61, 25]],
 [[[1, 3], [2, 8], [3, 6], [4, 5], [5, 8], [6, 7], [7, 8]], 
    [56, 4, 72, 26, 56, 98, 25, 98]], 
 [[[1, 7], [2, 5], [3, 7], [4, 8], [5, 9], [6, 9], [7, 6], [8, 6]], 
    [80, 24, 90, 8, 22, 8, 74, 2, 8]], 
 [[[1, 3], [2, 1], [3, 9], [4, 9], [5, 7], [6, 7], [7, 4], [8, 3]], 
    [32, 84, 84, 59, 9, 44, 37, 97, 89]], 
 [[[1, 6], [2, 5], [3, 2], [4, 5], [5, 10], [6, 8], [7, 4], [8, 5], [9, 10]], 
    [46, 46, 13, 93, 87, 50, 30, 29, 74, 56]]]
[[8, 5], [6, 4], [4, 3], [0, 0], [7, 5], [7, 5]]
        