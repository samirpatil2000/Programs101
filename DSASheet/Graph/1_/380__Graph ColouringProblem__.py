from typing import Dict, List
import collections
class Solution:
    def applyColour(self,src:int,graph,colour_to_vertices:List[int]):
        current_colours=[False]*len(graph)
        for e in graph[src]:
            if colour_to_vertices[e]!=-1:
                current_colours[colour_to_vertices[e]]=True
        for i in range(len(current_colours)):
            if current_colours[i]==False:
                break
        colour_to_vertices[src]=i
        return i
    def colourGraph(self,n,edges:List[List[int]]):
        graph={}
        for i in range(n+1):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        colour_to_vertices=[-1]*len(graph)
        max_=0
        for src in range(len(graph)):
            max_=max(max_,self.applyColour(src,graph,colour_to_vertices))
        return max_+1,colour_to_vertices
    
    
    
sol=Solution()
n=4
edges= [[0,1],[0,2],[0,4],[1,3],[2,3],[4,2],[4,1]]
print(sol.colourGraph(n,edges))


