from typing import List
import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations,values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)
        print(graph['x5'],)
        print(graph['x1'],)
        
        def dfs(u,v,visited):
            if u not in graph or v not in graph:
                return -1.0
            if v in graph[u]:
                return graph[u][v]
            
            for edge in graph[u]:
                if edge not in visited:
                    visited.add(edge)
                    temp=dfs(edge,v,visited)
                    if temp==-1.0:
                        continue
                    return graph[u][edge]*temp
            return -1.0
        
        result=[]
        for query in queries:
            result.append(dfs(query[0],query[1],set()))
        return result
                          
                    
                    
                
            
            
    
    
sol=Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
print(sol.calcEquation(equations,values,queries))

        



