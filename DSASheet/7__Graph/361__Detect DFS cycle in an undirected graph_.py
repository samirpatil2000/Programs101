# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph=defaultdict(list)
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
                       
    def detectCycle_DFS(self,visited,src):
        if visited[src]==True:
            return True
        visited[src]=True
        for i in self.graph[src]:
            if visited[i]==False:
                if self.detectCycle_DFS(visited,src):
                    return True
        return False 
    def detectCycle(self,visited):
        for i in self.graph.keys():
            if self.detectCycle_DFS(visited,i):
                return True
        return False    


g=Graph()
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(4,3)
g.add_edge(3,2)
g.printGraph()
visited=[False for _ in g.graph.keys()]
print(g.detectCycle(visited))
        
        