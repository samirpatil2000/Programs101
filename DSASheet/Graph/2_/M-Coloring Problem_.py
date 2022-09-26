# import collections

# def apply_colour(graph, src, colours_to_vertices):
#     current_colours = [False] * len(graph)
#     for e in graph[src]:
#         if colours_to_vertices[e] != -1:
#             current_colours[colours_to_vertices[e]] = True
#     colour = 0
#     for i in range(len(current_colours)):
#         if current_colours[i] == False:
#             colour = i
#             break
#     colours_to_vertices[src] = colour
#     return colour
 
        
            
    
# def graphColoring(edges, k, V):
#     graph = collections.defaultdict(list)
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
#     colour_to_vertices = [-1] * len(graph)
#     max_ = 0
#     for src in range(len(graph)):
#         max_ = max(max_, apply_colour(graph, src, colour_to_vertices) + 1)
#         if max_ > k:
#             return False
            
#     return True
# N = 4
# M = 3
# E = 5
# edges = [(0,1),(1,2),(2,3),(3,0),(0,2)]

# N = 3
# M = 2
# E = 3
# edges = [(0,1),(1,2),(0,2)]
# print(graphColoring(edges, M, E))

class Solution:
    
    def is_safe(self, graph, src, color, colours):
        for e in graph[src]:
            if colours[e] == color:
                return False
        return True
    
    def dfs(self, graph, src, colours, i, vertices):
        if src == vertices:
            return True
        
        for edge in graph[src]:
            if self.is_safe(graph, edge, i, colours):
                colours[edge] = i
                if self.dfs(graph, edge, colours, i + 1):
                    return True
                colours[edge] = 0
        return False
    
sol = Solution()
print(sol.dfs(graph, ))
                
            
        