from typing import List, get_args

class Solution:
    
    def toposort_BFS(self,graph:dict,nodes:int):        
        
        indegrees=[0]*(nodes+1)
        for src in graph.keys():
            for e in graph[src]:
                indegrees[e]+=1
                
        queue=[]
        result=[]
        if len(set(indegrees))==1: 
            if indegrees[0]!=0:
                return "Cycle" ,True
            
            
        for i in range(len(indegrees)):
            if indegrees[i]==0:
                queue.append(i)
                result.append(i)
        
        while queue:
            src=queue.pop(0)
            for e in graph[src]:
                indegrees[e]-=1
                if indegrees[e]==0:
                    queue.append(e)
                    result.append(e)
        print(indegrees)
        return result[::-1],"Cycle",len(set(indegrees))==2
    
    
    def toposort_DFS(self,graph,nodes):
        visited=set()
        result=[]
        def dfs(src):
            visited.add(src)
            for edge in graph[src]:
                if edge not in visited:
                    dfs(edge)
            result.append(src)
        
        for src in graph.keys():
            if src not in visited:
                visited.add(src)
                dfs(src)
    
        return result
        
            
        
    
                
                


nodes=6
edges=[[0,3],[0,1],[1,2],[2,3],[5,3],[5,4],[5,6],[4,6]]  # the toposort

edges=[[3,0],[0,1],[1,2],[2,3],[5,3],[5,4],[5,6],[4,6]]  # the cycle

nodes=3
edges=[[0,1],[1,2],[2,3],[3,0]]

graph={i:[] for i in range(nodes+1)}
for u,v in edges:
    graph[u]=graph.get(u,[])+[v]

print(graph)
    
sol=Solution()  
print(sol.toposort_BFS(graph,nodes))

print(sol.toposort_DFS(graph,nodes))
            
        