from collections import defaultdict
from typing import Counter

class Graph:
    
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices+1
    
        for i in range(self.vertices):
            self.graph[i]=[]
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
                       
    def detectCycle_BFS_TopologicalSort(self,visited,src):
        queue=[src]
        count_=0
        while(len(queue)>0):
            temp=queue.pop(0)
            if visited[temp]==True:
                return True
            visited[temp]=True
            count_+=1
            for i in self.graph[temp]:
                if visited[i]==False:
                    queue.append(i)
                    
        print(count_)
        if count_==self.vertices:
            print("Their is no cycle")
            return False
        return True
                    
            
    def detectCycle(self,visited):
        print([i for i in self.graph.keys()])
        for i in self.graph.keys():
        
            # print("chas",i)
            if visited[i]==False:
                if self.detectCycle_BFS_TopologicalSort(visited,i):
                    return True
                
        return False    


g=Graph(3)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(0,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.printGraph()
visited=[False for _ in range(g.vertices)]

# print(visited,in_curr)/
print(g.detectCycle(visited))
        
        