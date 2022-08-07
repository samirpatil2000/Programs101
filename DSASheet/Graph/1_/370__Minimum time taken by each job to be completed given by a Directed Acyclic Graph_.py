# https://www.geeksforgeeks.org/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/

import collections
class Graph:
    
    def __init__(self,n) -> None:
        self.graph=collections.defaultdict(list)
        self.v=n+1
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def minTime(self):
        result={}
        indegrees={}
        visited={}
        for i in range(1,self.v):
            indegrees[i]=0
            visited[i]=False
        for i in range(1,self.v):
            for j in self.graph[i]:
                indegrees[j]+=1
        queue=[]
        for i in indegrees.keys():
            if indegrees[i]==0:
                queue.append(i)
                result[i]=1
        
        while queue:
            temp=queue.pop(0)
            visited[temp]=True
            for i in self.graph[temp]:
                if visited[i]==False:
                    indegrees[i]-=1
                    if indegrees[i]==0:
                        result[i]=result[temp]+1
                        queue.append(i)
        
        return result
n=10
g=Graph(n) 
    
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 8)
g.add_edge(2, 9)
g.add_edge(3, 6)
g.add_edge(4, 6)
g.add_edge(4, 8)
g.add_edge(5, 8)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 10)

print(g.minTime().values())
# 1 1 2 2 2 3 4 5 2 6 
        
            
        
        
        