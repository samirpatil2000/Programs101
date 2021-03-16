

from typing import Counter


class Node:
    def __init__(self,src,nbr,wt):
        self.src=src
        self.nbr=nbr
        self.wt=wt
        self.next=None

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices 
        self.graph = [None] * (self.vertices+1)  # it is just a list 
    
    def add_edge(self,src,nbr,wt):
        node=Node(src,nbr,wt)
        node.next=self.graph[src]
        self.graph[src]=node
         
        node=Node(nbr,src,wt)
        node.next=self.graph[nbr]
        self.graph[nbr]=node
    
    def print_graph(self):
        # print(self.vertices)
        for i in range(self.vertices):
            print(f"head({i})",end=" ")
            temp=self.graph[i]
            while(temp):
                # print("->",temp.wt)
                print(f"--> {temp.src}-{temp.nbr} W {temp.wt}",end=" ")
                temp=temp.next
            print()
    def get_nbr(self,i):
        temp=self.graph[i]
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
    def get_node(self,i):
        return self.graph[i]




# THIS is for input 

v=5
graph_=Graph(v)   
graph_.add_edge(0,1,10)
graph_.add_edge(1,2,10)
graph_.add_edge(2,3,10)
graph_.add_edge(3,4,10)

#FALSE Pentagon
# graph_.add_edge(4,0,10)
#TRUE Hexagon
graph_.add_edge(4,5,10)
graph_.add_edge(5,0,10)
graph_.print_graph()





def bfSearch(graph,src,visited):
    queue=[]
    queue.append([src,str(src)+"",0])

    while(len(queue)>0):
        # r *m w *a
        arr=queue.pop(0)
        if(visited[arr[0]]!=-1):
            if(arr[2]!=visited[arr[0]]):
                return False
        else:
            visited[arr[0]]=arr[2]#level
        edge_=graph_.get_node(arr[0])
        while(edge_):
            if(visited[edge_.nbr]==-1):
                queue.append([edge_.nbr,arr[1]+str(edge_.nbr),arr[2]+1])
            edge_=edge_.next
    return True
        
        

visited=[-1 for _ in range(v+1)]
def isBipartite(graph,visited):
    for i in range(v+1):
        if visited[i]==-1:
            isComBipartite=bfSearch(graph,i,visited)
            if(isComBipartite == False):
                return False
    return True

print(isBipartite(graph_,visited))