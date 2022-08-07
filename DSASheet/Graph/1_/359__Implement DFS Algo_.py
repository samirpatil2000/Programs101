
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
            
    # self.visited=
    def dfs(self,src,visited):
        visited.add(src)
        print(src,end=" ")
        for i in self.graph[src]:
            if i not in visited:
                self.dfs(i,visited)
    

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.printGraph()

visited=set()
g.dfs(2,visited)

        