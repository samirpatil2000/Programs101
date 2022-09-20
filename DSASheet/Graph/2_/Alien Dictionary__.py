import collections
class Solution:
    
    result = []
    
    def create_graph(self, words, K):
        graph = {chr(i + 97) : [] for i in range(K)}
        for i in range(len(words) - 1):
            j = 0
            min_len = min(len(words[i]), len(words[i + 1]))
            while j < min_len and words[i][j] == words[i + 1][j]:
                j += 1
            if j < min_len:
                graph[words[i + 1][j]].append(words[i][j])
        return graph
    
    def toposort(self, graph, src, visited):
        visited.add(src)
        for edge in graph[src]:
            if edge not in visited:  
                self.toposort(graph, edge, visited)
        self.result.append(src)
     
    def findOrder(self, words, N, K):
        
        graph = self.create_graph(words, K)
        print(graph)
        visited = set()
        for src in graph:
            if src not in visited:
                self.toposort(graph, src, visited)
        return self.result



sol = Solution()
words = ["baa", "abcd", "abca", "cab", "cad"]
words = ["caa","aaa","aab"]
print(sol.findOrder(words, 3, 3))