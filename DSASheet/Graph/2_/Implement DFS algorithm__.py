import collections
from pydoc import visiblename
class Solution:
    
    def make_graph(self, edges):
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        return graph
    
    def dfs_with_st(self,  graph):
        st = []
        visited = set()
        st = [0]
        result = []
        while st:
            src = st.pop()
            if src in visited:
                continue
            visited.add(src)
            result.append(src)
            for edge in graph[src]:
                st.append(edge)
        return result
    def dfs(self, graph):
        visited = set()
        result = []
        def helper(src, visited):
            if src in visited:
                return
            visited.add(src)
            result.append(src)
            for edge in graph[src]:
                helper(edge, visited)
        helper(0, visited)
        return result
    

            
    

            
            
            
            
        
            
        

vertices = 4
edges = [[1,3],[1,4],[2,3],[2,4],[4,3]]
sol = Solution()
graph=sol.make_graph(edges)
print(sol.dfs(graph))
print(sol.dfs_with_st(graph))