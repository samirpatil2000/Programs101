from typing import List
import collections,math
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        graph=collections.defaultdict(list)
        for u,v,t in roads:
            graph[u].append([v,t])
            graph[v].append([u,t])
            
        MOD=1e9+7
        minHeap=[[0,0]]  # dist,src
        dist=[math.inf]*n
        ways=[0]*n
        ways[0]=1
        dist[0]=0
        while minHeap:
            d,src=heapq.heappop(minHeap)
            if dist[src]<d:continue
            for e,t in graph[src]:
                if dist[e]>d+t:
                    dist[e]=d+t
                    ways[e]=ways[src]
                    heapq.heappush(minHeap,[dist[e],e])
                elif dist[e]==d+t:
                    ways[e]+=ways[src]
                    ways[e]%=MOD
                    # ways[e] = (ways[e] + ways[src]) % 1_000_000_007
        return int(ways[-1])

sol=Solution()
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

n,roads=6,[[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]]
print(sol.countPaths(n,roads))
                
                    