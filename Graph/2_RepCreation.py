class Node:
    def __init__(self,src,dest,wt):
        self.src=src
        self.dest=dest
        self.wt=wt
        self.next=None

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices 
        self.graph = [None] * self.vertices  # it is just a list 
    
    def add_edge(self,src,dest,wt):
        node=Node(src,dest,wt)
        node.next=self.graph[src]
        self.graph[src]=node
         
        node=Node(dest,src,wt)
        node.next=self.graph[dest]
        self.graph[dest]=node
    
    def print_graph(self):
        for i in range(self.vertices):
            print(f"head({i})",end=" ")
            temp=self.graph[i]
            while(temp):
                # print("->",temp.wt)
                print(f"--> {temp.src}-{temp.dest} W {temp.wt}",end=" ")
                temp=temp.next
            print()


graph=Graph(7)
graph.add_edge(0,3,10)
graph.add_edge(0,1,10)
graph.add_edge(1,2,10)
graph.add_edge(2,3,10)
graph.add_edge(3,4,10)
graph.add_edge(4,6,10)
graph.add_edge(4,5,10)
graph.add_edge(5,6,10)
graph.print_graph()

