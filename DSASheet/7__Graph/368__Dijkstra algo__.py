# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict
from typing import Tuple

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
    
    def getMin(arr):
        min_=-2*32
        # for i in range(arr):
        #     if arr[i][]
        
    
    def Dijkstra(src):
        queue=[[src,""+str(src)]]
        


n = 5
connections = [[0,1],[0,2],[3,4],[2,3]] 

g=Graph(n)
for i in connections:
    g.add_edge(i[0],i[1])
    
g.printGraph()

print(g.getConnection(n))



                
            
            
        