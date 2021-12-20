from typing import List
from collections import defaultdict

class Solution:
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==0:return []
        if n==1:return [0]
        degree=[0]*n
        graph=defaultdict(set)
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
            
            graph[v].add(u)
            graph[u].add(v)
        queue=[]
        for i in range(n):
            if degree[i]==1:queue.append(i)
        count=n
        while count>2:
            size=len(queue)
            count-=size
            while size:
                size-=1
                temp=queue.pop(0)
                for conn in graph[temp]:
                    degree[conn]-=1
                    # graph[conn].remove(temp)
                    if degree[conn]==1:
                        queue.append(conn)
        return queue
    
    
sol=Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print(sol.findMinHeightTrees(n,edges))
                
        