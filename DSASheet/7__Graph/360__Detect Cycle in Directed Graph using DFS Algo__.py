# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-directed-graph/1
from collections import defaultdict

class Graph:
    
    def __init__(self,vertices):
        self.graph={} #defaultdict(list)
        self.vertices=vertices+1
    
        for i in range(self.vertices):
            self.graph[i]=[]
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
                       
    def detectCycle_DFS(self,visited,src,in_curr):
        if visited[src]==True and in_curr[src]==True:
            print(src)
            return True
        visited[src]=True
        in_curr[src]=True
        for i in self.graph[src]:
            if visited[i]==False:
                if self.detectCycle_DFS(visited,i,in_curr):
                    return True
            elif in_curr[i]==True:
                print(i)
                return True
        in_curr[src]=False
        return False 
    def detectCycle(self,visited,in_curr):
        for i in self.graph.keys():
            print("chas",i)
            if visited[i]==False:
                if self.detectCycle_DFS(visited,i,in_curr):
                    return True
        return False    


g=Graph(3)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(0,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.printGraph()
visited=[False for _ in g.graph.keys()]
in_curr=[False for _ in g.graph.keys()]
print(g.detectCycle(visited,in_curr))
        
        