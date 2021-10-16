from typing import List

class Solution:
    
    def toposort(self,nodes:int,edges:List[List[int]]):
        graph={i:[] for i in range(nodes+1)}
        for u,v in edges:
            graph[u]=graph.get(u,[])+[v]
        print(graph)
        indegrees=[0]*(nodes+1)
        for src in graph.keys():
            for e in graph[src]:
                indegrees[e]+=1
                
        queue=[]
        result=[]
        for i in range(len(indegrees)):
            if indegrees[ i]==0:
                queue.append(i)
                result.append(i)
        
        while queue:
            src=queue.pop(0)
            for e in graph[src]:
                indegrees[e]-=1
                if indegrees[e]==0:
                    queue.append(e)
                    result.append(e)
        return result[::-1]
    
                
                


nodes=6
edges=[[0,3],[0,1],[1,2],[2,3],[5,3],[5,4],[5,6],[4,6],[5,0]]  # the toposort
      
sol=Solution()  
print(sol.toposort(nodes,edges))
            
        