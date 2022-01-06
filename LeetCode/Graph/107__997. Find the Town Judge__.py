import typing
from collections import defaultdict

from typing import List
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        for u,v in trust:
            graph[u].append(v)
        print(graph)
        for i in range(1,n+1):
            if i not in graph or len(graph[i])==0:
                return i
            
        return -1
    
        # graph={}
        # for i in range(1,N+1):
        #     graph[i]=[]
        # for u,v in trust:
        #     graph[u].append(v)
        # indg=[0]*(N+1)
        # for i in range(1,N+1):
        #     for edge in graph[i]:
        #         indg[edge]+=1
        # print(indg[1:])
        # max_=0
        # for i in range(1,len(indg)):
        #     if indg[i]>max_:
        #         max_=indg[i]
        #         if max_==N-1 and len(graph[i])==0:
        #             return i
                
        # return -1 
    
                
                
                
            
        
    
    
sol=Solution()
n = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
n = 3
trust = [[1,3],[2,3],[3,1]]
trust = [[1,2],[2,3]]

print(sol.findJudge(n,trust))