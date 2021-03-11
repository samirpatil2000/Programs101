

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
graph_.add_edge(0,3,10)
graph_.add_edge(0,1,10)
graph_.add_edge(1,2,10)
graph_.add_edge(2,3,10)
graph_.add_edge(3,4,10)
graph_.add_edge(4,6,10)
graph_.add_edge(2,5,10)
graph_.add_edge(4,5,10)
graph_.add_edge(5,6,10)
graph_.print_graph()



bool_arr=[False for _ in range(v+1)]
def printHamiltonianPathsANDCycles(graph,src,output_str,visited_arr,count,orgsrc):
    if(count==graph.vertices):
        temp_=graph.get_node(src)
        while(temp_):
            if(orgsrc==temp_.nbr):
                print("Cycle : ",output_str)
                return
            temp_=temp_.next   
        print("Path : ",output_str)
        return
    visited_arr[src]=True
    temp=graph.get_node(src)
    while(temp):
        if visited_arr[temp.nbr]==False:
            printHamiltonianPathsANDCycles(graph,temp.nbr,output_str+str(temp.nbr),visited_arr,count+1,orgsrc)
        temp=temp.next
    visited_arr[src]=False
    return
        
printHamiltonianPathsANDCycles(graph_,0,"0",bool_arr,0,0)
