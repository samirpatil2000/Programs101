# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

from collections import defaultdict
from typing import Tuple

class Graph:
    
    def __init__(self,n):
        self.graph=defaultdict(list)
        
        # for i in range(n):
        #     self.graph[i]=[]
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
                       
    def getConnection(self,n,visited):
        if len(connections) < n - 1: return -1
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
        return count_-1


n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]

g=Graph(n)
for i in connections:
    g.add_edge(i[0],i[1])
    
g.printGraph()
visited=[False for _ in range(n)]
print(g.getConnection(n,visited))



class Solution():
    def makeConnected(self, n, connections):
        graph=[set() for _ in range(n)]
        
        for edge in connections:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        visited=set()
        print(graph)
        
        def getCompo(src):
            visited.add(src)
            for i in graph[src]:
                if i not in visited:
                    getCompo(i)
        def getConnectedCompo():
            if len(connections) < n - 1: return -1
            connected_compo=0
            for i in range(len(graph)):
                if i not in visited:
                    getCompo(i)
                    connected_compo+=1
            return connected_compo-1
        return getConnectedCompo()
    
sol=Solution()
print(sol.makeConnected(n,connections))
                
            
            
        