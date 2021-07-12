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

v=6
graph_=Graph(v)
graph_.add_edge(0,3,40)
graph_.add_edge(0,1,10)
graph_.add_edge(1,2,10)
graph_.add_edge(2,3,10)
graph_.add_edge(3,4,2)
graph_.add_edge(4,6,8)
graph_.add_edge(4,5,3)
graph_.add_edge(5,6,3)
graph_.print_graph()


bool_arr=[False for i in range(v+1)]
# print(bool_arr)




list=[[]]
def printAllPaths(graph,src,dest,visited,psf,wtsf):
    if(src==dest):
        list.append([psf,wtsf])
        print(psf,"W",wtsf)
        return
    visited[src]=True
    temp=graph.get_node(src)
    while(temp):
        if(visited[temp.nbr]==False):
            printAllPaths(graph,temp.nbr,dest,visited,psf+str(temp.nbr),wtsf+temp.wt)
        temp=temp.next
    visited[src]=False
    return

printAllPaths(graph_,0,6,bool_arr,str(0)+"",0)
print(list[1:])