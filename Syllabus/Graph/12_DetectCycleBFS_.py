

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

v=6
graph_=Graph(v)   
# graph_.add_edge(0,3,10)
# graph_.add_edge(0,1,10)
# graph_.add_edge(1,2,10)
# graph_.add_edge(2,3,10)
# graph_.add_edge(3,4,10)
# graph_.add_edge(4,6,10)
# graph_.add_edge(2,5,10)
# graph_.add_edge(4,5,10)
# graph_.add_edge(5,6,10)
graph_.add_edge(0,1,10)
graph_.add_edge(2,3,10)
graph_.add_edge(4,5,10)
graph_.add_edge(5,6,10)
graph_.add_edge(4,6,10)
graph_.print_graph()




        
def isCycle(graph,src,visited):
    queue=[]
    queue.append([src,str(src)+""])
    
    while(len(queue)>0):
        # Remove *Mark W *Add
        arr=queue.pop(0)
        if(visited[arr[0]]==True):
            # we found the cycle
            return True
        visited[arr[0]]=True
        edge=graph.get_node(arr[0])
        
        while(edge):
            if(visited[edge.nbr]==False):
                queue.append([edge.nbr,arr[1]+str(edge.nbr)])
            edge=edge.next
    return False


visited=[False for _ in range(v+1)]
def CycleChecker(graph,v,visited):
    for i in range(v+1):
        if(visited[i]==False):
            cycle=isCycle(graph,i,visited)
            if(cycle):
                return True
    return False

print(CycleChecker(graph_,v,visited))


        

            
        