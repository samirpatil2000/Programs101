from collections import defaultdict
import collections


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
    
    def pop(self,queue,visited):
        min_wt=2**32
        min_index=0
        for i in range(len(queue)):
            if queue[i][2]<min_wt and queue[i][0] not in visited:
                min_wt=queue[i][2]
                min_index=i
        item=queue[min_index]
        del queue[min_index]
        return item
            

    def miniumSpanningTrees(self,src):
        visited=set()
        queue=[]
        queue.append([src,str(-1),0])
        while queue:
            
            temp=self.pop(queue,visited)
            if temp[0] in visited:
                continue
            print(temp)
            visited.add(temp[0])
            for i in self.graph[temp[0]]:
                if i not in visited:
                    queue.append([i.src,temp[0],i.wt])
                    
             
v=8
connections=[
    # [0,3,40],
    # [0,1,10],
    # [1,2,10],
    # [3,2,10],
    # [4,3,3],
    # [4,6,8],
    # [4,5,3],
    # [5,6,3],
    
    [0,1,4],
    [0,7,8],
    [1,7,11],
    [1,2,8],
    [2,8,2],
    [7,8,7],
    [7,6,1],
    [5,6,2],
    [8,6,6],
    [2,5,4],
    [2,3,7],
    [4,3,9],
    [3,5,14],
    [4,5,10],
    
    #another graph
]
g=Graph(v,connections)
# g.printGraph()
g.miniumSpanningTrees(0)
            