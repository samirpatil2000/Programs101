import collections
class Solution:
    
    def make_graph(self, edges, vertices):
        
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        return graph
    
    def bfs(self, edges, vertices):
        graph = self.make_graph(edges, vertices)
        queue = collections.deque()
        queue.append(0)
        result = []
        visited = set()
        while queue:
            src = queue.popleft()
            if src in visited:
                continue
            result.append(src)
            visited.add(src)
            for edge in graph[src]:
                queue.append(edge)
        return result

vertices = 4
edges = [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(Solution().bfs(edges, vertices))