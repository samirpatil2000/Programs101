
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph={}
        for i in range(1,n+1):
            graph[i]=[]
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
        colour_={}
        def dfs(src:int,colour):
            current_colour=[False]*(n+1)
            for e in graph[src]:
                if e in colour:
                    current_colour[colour[e]]=True
            for i in range(1,5):
                if current_colour[i]==False:
                    break
            colour[src]=i
        
        for src in range(1,n+1):
            dfs(src,colour_)
        return colour_.values()

sol=Solution()
n = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(sol.gardenNoAdj(n,paths))
                            