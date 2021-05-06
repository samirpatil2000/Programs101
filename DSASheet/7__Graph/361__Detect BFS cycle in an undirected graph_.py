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
            
    def isCycle(self,src,visited):
        queue=[src]
        while(len(queue)>0):
            temp=queue.pop(0)
            if visited[temp]:
                return True
            visited[temp]=True
            for i in self.graph[temp]:
                if visited[i]==False:
                    queue.append(i)
            
            
    def detectCycleBFS(self):
        visited=[False for _ in self.graph.keys()]
        for i in self.graph.keys():
            if visited[i]==False:
                if self.isCycle(i,visited):
                    return True
                
        return False
                
            
        


g=Graph()
g.add_edge(0,1)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(4,3)
g.add_edge(3,2)
g.printGraph()  
print(g.detectCycleBFS())
        
        