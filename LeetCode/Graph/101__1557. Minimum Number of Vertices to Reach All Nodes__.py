from typing import List
from collections import deque

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph={}
        indegrees=[0]*n
        for i in range(n):
            graph[i]=[]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        for i in range(n):
            for edge in graph[i]:
                indegrees[edge]+=1
        q=[]
        print(indegrees)
        for ind in range(n):
            for i in range(n):
                print(indegrees[i],ind)
                if indegrees[i]==ind:
                    q.append(i)
                    
            if len(q)>0:
                return q
                
sol=Solution()
n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
print(sol.findSmallestSetOfVertices(n,edges))
                    
            