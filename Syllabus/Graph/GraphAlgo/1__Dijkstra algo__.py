from collections import defaultdict
import heapq

class Node():
    def __init__(self,src,wt) -> None:
        self.src=src
        self.wt=wt
        

class Graph():
    def __init__(self,vertices,list_) -> None:
        self.graph={}
        self.vertices=vertices+1
        
        for i in range(self.vertices):
            self.graph[i]=[]
    
        for edge in list_:
            self.graph[edge[0]].append(Node(edge[1],edge[2]))
            self.graph[edge[1]].append(Node(edge[0],edge[2]))
            
    def printGraph(self):
        for i in self.graph.keys():
            x=self.graph[i]
            print(i,[(k.wt,k.src) for k in x])
    
    
            

    def DijkstraUsingHeap(self,src):
        list_=[]
        queue=[[0,src]]
        heapq.heapify(queue)
        visited=set()
        
        while queue:
            temp=heapq.heappop(queue)
            if temp[1] in visited:
                continue
            visited.add(temp[1])
            list_.append([temp[1],temp[0]])
            for node in self.graph[temp[1]]:
                if node.src not in visited:
                    heapq.heappush(queue,[temp[0]+node.wt , node.src])            
        
        return list_
v=8
connections=[
    [0,3,40],
    [0,1,10],
    [1,2,10],
    [3,2,10],
    [4,3,3],
    [4,6,8],
    [4,5,3],
    [5,6,3],
    
    # [0,1,4],
    # [0,7,8],
    # [1,7,11],
    # [1,2,8],
    # [2,8,2],
    # [7,8,7],
    # [7,6,1],
    # [5,6,2],
    # [8,6,6],
    # [2,5,4],
    # [2,3,7],
    # [4,3,9],
    # [3,5,14],
    # [4,5,10],
    
    #another graph
]
g=Graph(v,connections)
x=g.DijkstraUsingHeap(0)
x.sort(key=lambda x:x[0])
print(x)
            