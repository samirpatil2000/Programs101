from collections import defaultdict
import collections


class Node():
    def __init__(self,src,wt) -> None:
        self.src=src
        self.wt=wt
        
class Graph():
    # def __init__(self,vertices) -> None:
    #     self.V=vertices
    #     self.graph=[]
    
    # def add_edge(self,u,v,wt):
    #     self.graph.append([u,v,wt])
        
    
    
    def findParent(self,node,parent):
        if node==parent[node]:
            return node
        parent[node]=self.findParent(parent[node],parent)
        return parent[node]
            
    def union(self,u,v,parent,rank):
        u_root=self.findParent(u,parent)
        v_root=self.findParent(v,parent)
        
        if rank[u_root]<rank[v_root]:
            parent[u_root]=v_root
        elif rank[u_root]>rank[v_root]:
            parent[v_root]=u_root
        else:
            rank[v_root]+=1
            parent[u_root]=v_root
        
            
        

    def kruksalAlgo(self,connections,vertices):
        result=[]
        rank=[]
        parent=[]
        for i in range(vertices+1):
            parent.append(i)
            rank.append(0)
        print(parent)
        connections.sort(key=lambda it:it[2])
        for con in connections:
            x=self.findParent(con[0],parent)
            y=self.findParent(con[1],parent)
            if x!=y:
                result.append(con)
                self.union(con[0],con[1],parent,rank)
                
        return result
            
        
                    
             
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

# connections.sort(key=lambda connections:connections[2])
# print(connections)
sol=Graph()
print(sol.kruksalAlgo(connections,v))

            