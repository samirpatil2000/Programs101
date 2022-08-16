import heapq
class Solution:
    def shortest_path(self, graph, src):
        result = []
        queue = [[0, src]]
        heapq.heapify(queue)
        distances = {vertex: float("infinity") for vertex in graph.keys()}
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            result.append([current_vertex, current_distance])
            for edge, distance in graph[current_vertex].items():
                if distances[edge] > current_distance + distance:
                    distances[edge] = current_distance + distance
                    heapq.heappush(queue, [distances[edge], edge])            
        return result
    
    def dijkstra(self, V, graph, src):
        #code here
        result = []
        queue = [[0, src]]
        heapq.heapify(queue)
        distances = {vertex: float("infinity") for vertex in range(V)}
        distances[src] = 0
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            if current_distance > distances[current_vertex]:
                continue
            for edge, distance in graph[current_vertex]:
                if distances[edge] > current_distance + distance:
                    distances[edge] = current_distance + distance
                    heapq.heappush(queue, [distances[edge], edge])         
        return distances.values()
    
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}


sol = Solution()
# print(sol.shortest_path(example_graph, src="X"))
V = 2
src = 0
graph = [[[1, 9]] , [[0, 9]]] 
graph = [
            [[3, 9], [5, 4]], # 0
            [[4, 4]],         # 1
            [[5, 10]],        # 2
            [[0, 9]],         # 3
            [[1, 4], [5, 3]], # 4
            [[0, 4], [2, 10], [4, 3]] # 5
        ]
src = 1
V = 6 
print(sol.dijkstra(V, graph, src))

# 6 5
# 0 3 9
# 0 5 4
# 1 4 4
# 2 5 10
# 4 5 3


# v, e = [int(i) for i in input().split(' ')]
# graph = [[] for _ in range(v)]
# for _ in range(e):
#     u, v, w = [int(i) for i in input().split(' ')]
#     graph[u].append([v, w])
#     graph[v].append([u, w])
# print(graph)
    
    
# N,M,T,C=[int(i) for i in n.split(' ')]
# graph=collections.defaultdict(list)
# while M:
#     M-=1
#     n=input()
#     u,v=[int(i) for i in n.split(' ')]
#     graph[u].append(v)
#     graph[v].append(u)
