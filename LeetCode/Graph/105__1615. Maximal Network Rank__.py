from typing import Counter, List
import collections
class Solution():
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph={}
        for i in range(n):
            graph[i]=set()
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
        max_=0
        for city1 in range(n):
            for city2 in range(n):
                if city1==city2:
                    continue
                count_=0
                if city1 in graph[city2]:
                    count_=1
                max_=max(max_,len(graph[city1])+len(graph[city2])-count_)
        
        return max_
    
sol=Solution()
n = 8
roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(sol.maximalNetworkRank(n,roads))
            

        