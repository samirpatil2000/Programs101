from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[-1]*len(graph)
        
        def bfs(src,graph):
            q=[[src,0]]
            while q:
                temp,level=q.pop(0)
                if visited[temp]!=-1:
                    if visited[temp]!=level:
                        # print(temp,level)
                        return False
                else:
                    visited[temp]=level
                    
                for edge in graph[temp]:
                    if visited[edge]==-1:
                        q.append([edge,level+1])
            return True
                        
                    
        
        for i in range(len(graph)):
            if visited[i]==-1:
                if bfs(i,graph)==False:
                    return False
        return True
    
    
sol=Solution()
graph =[[1,3],[0,2],[1,3],[0,2]]
print(sol.isBipartite(graph))