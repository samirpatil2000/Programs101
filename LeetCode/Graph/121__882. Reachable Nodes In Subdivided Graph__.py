from typing import List
import heapq
import collections

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph=collections.defaultdict(dict)
        for u,v,wt in edges:
            graph[u][v]=graph[v][u]=wt
        queue=[[-maxMoves,0]]
        heapq.heapify(queue)
        
        result=0
        visited=set()
        while queue:
            maxreach,src=heapq.heappop(queue)
            maxreach*=-1
            print(maxreach)
            
            
            if src in visited:
                continue
            visited.add(src)
            result+=1
            for e in graph[src].keys():
                if e not in visited:
                    print(graph[src][e],graph[src])
                    if maxreach>=graph[src][e]+1:
                        heapq.heappush(queue,[-(maxreach-graph[src][e]-1),e])
                    reachable_nodes=min(maxreach,graph[src][e])
                    
                    # if result==1:result+=1
                    result+=reachable_nodes
                    graph[src][e]-=reachable_nodes
                    # graph[e][src]-=reachable_nodes
        return result
    
    

                    
                
            

sol=Solution()
edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6
n = 3

edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
maxMoves = 10
n = 4

# edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
# maxMoves = 17
# n = 5
print(sol.reachableNodes(edges,maxMoves,n))
        
        