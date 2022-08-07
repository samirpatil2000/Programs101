from typing import DefaultDict


from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices
    
        for i in range(self.vertices):
            self.graph[i+1]=[]
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])

graph=Graph(5)
graph.add_edge(1,2)
# graph.print_adj_list()
graph.add_edge(4,2)
graph.add_edge(3,2)
graph.add_edge(5,4)
graph.add_edge(5,1)
graph.printGraph()