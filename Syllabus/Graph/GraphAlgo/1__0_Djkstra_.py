from heapq import heappush,heappop,heapify
from typing import List


class Solution:
    
    def Dijkstra(self,edges:List[List[int]],nodes:int):
        graph={node:[] for node in range(nodes)}
        for u,v,wt in edges:
            graph[u].append([v,wt])
            graph[v].append([u,wt])
        
        print(graph)
        q=[[0,"0",0]]
        heapify(q)
        visited=set()
        while q:
            src,str_,wt=heappop(q)
            if src in visited:
                continue
            visited.add(src)
            print(src,str_,wt)
            for e,e_wt in graph[src]:
                if e in visited:
                    continue
                heappush(q,[e,str_+"-"+str(e),wt+e_wt])
        

sol=Solution()
nodes=7
edges=[
    [0,3,40],
    [0,1,10],
    [1,2,10],
    [3,2,10],
    [4,3,3],
    [4,6,8],
    [4,5,3],
    [5,6,3],
]
print(sol.Dijkstra(edges,nodes))