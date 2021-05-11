# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict

class Graph:
    
    def __init__(self,n):
        self.graph={}
        
        for i in range(n):
            self.graph[i]=[]
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
                       
    def getConnection(self,n,visited):
        def getCompo(src,visited):
            # print(src)
            visited[src]=True
            for i in self.graph[src]:
                if visited[i]==False:
                    getCompo(i,visited)            
        
        
        count_ = 0
        for i in range(n):
            if visited[i] == False:
                count_ += 1
                visited[i]=True
                getCompo(i,visited)
        return count_


n = 5
connections = [[0,1],[0,2],[3,4],[2,3]]  

g=Graph(n)
for i in connections:
    g.add_edge(i[0],i[1])
    
g.printGraph()
visited=[False for _ in g.graph.keys()]
print(g.getConnection(n,visited))