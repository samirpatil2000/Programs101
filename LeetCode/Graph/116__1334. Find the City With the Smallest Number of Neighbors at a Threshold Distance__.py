from typing import List
import queue as Q
import heapq

class Node():
    def __init__(self,dest,wt):
        self.dest=dest
        self.wt=wt
        

class Solution():
    def pop(self,queue,visited):
        min_wt=2**32
        min_index=0
        for i in range(len(queue)):
            if queue[i][1]<min_wt and queue[i][0] not in visited:
                min_wt=queue[i][1]
                min_index=i
        item=queue[min_index]
        del queue[min_index]
        return item
    def bfs(self,graph,src,distanceThreshold):
        count_=0
        visited=set()
        # q=Q.PriorityQueue()
        
        q=[[0,src]]
        heapq.heapify(q)
        
        # visited.add(src)
        while q:
            # temp,tar_sum=self.pop(q,visited)
            tar_sum,temp=heapq.heappop(q)
            if temp in visited:
                continue
            if tar_sum>distanceThreshold:
                continue
            visited.add(temp)
            if tar_sum<=distanceThreshold and src!=temp:
                # print(src,temp,tar_sum)
                count_+=1
            for edge,wt in graph[temp]:
                if edge not in visited:
                    # q.append([edge,tar_sum+wt])
                    heapq.heappush(q,[tar_sum+wt,edge])
        return count_
    def printGraph(self,graph):
        for temp in range(len(graph)):
            print(temp,graph[temp])
        
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph={}
        for i in range(n):
            graph[i]=[]
        for u,v,wt in edges:
            graph[u].append([v,wt])
            graph[v].append([u,wt])
        max_city=0
        min_count=2**32
        for i in range(n):
            current_count=self.bfs(graph,i,distanceThreshold)
            print(i,current_count,min_count,max_city)
            if min_count>current_count:
                min_count=current_count
                max_city=i
            elif min_count==current_count:
                max_city=max(i,max_city)
        # self.printGraph(graph)       
        return max_city,min_count       
sol=Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
n=6
edges=[[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
distanceThreshold=20

print(sol.findTheCity(n,edges,distanceThreshold))
        