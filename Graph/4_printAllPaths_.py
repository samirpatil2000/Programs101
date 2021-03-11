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
graph_.add_edge(0,3,10)
graph_.add_edge(0,1,10)
graph_.add_edge(1,2,10)
graph_.add_edge(2,3,10)
graph_.add_edge(3,4,10)
graph_.add_edge(4,6,10)
graph_.add_edge(4,5,10)
graph_.add_edge(5,6,10)
graph_.print_graph()


bool_arr=[False for i in range(v+1)]
print(bool_arr)

# print(graph.get_nbr(0))
def Test(graph,src,dest):
    # if(src==dest):
    #     return True
    for i in range(graph.get_nbr(src)):
        temp=graph.get_node(src)
        while(temp):
            print(temp.src, end=",")
            temp=temp.next
        print()
# Test(graph_,2,3)


def printAllPaths(graph,src,dest,visited,psf):
    if(src==dest):
        print(psf)
        return
    visited[src]=True
    temp=graph.get_node(src)
    while(temp):
        # print(temp.nbr)
        if(visited[temp.nbr]==False):
            printAllPaths(graph,temp.nbr,dest,visited,psf+str(temp.nbr))
        temp=temp.next
    visited[src]=False
    return

printAllPaths(graph_,0,6,bool_arr,str(0)+"")


print(Test(graph_,0,6))