class Graph:
    def __init__(self,Vertices):
        self.vertices=Vertices
        self.adj_list={}
        
        for i in self.vertices:
            self.adj_list[i]=[]
            
    def add_edge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def print_adj_list(self):
        for i in self.vertices:
            print(i,"->",self.adj_list[i])
            
nodes=[1,2,3,4,5]
graph=Graph(nodes)
graph.print_adj_list()
print("\n")
graph.add_edge(1,2)
graph.add_edge(4,2)
graph.add_edge(3,2)
graph.add_edge(5,4)
graph.add_edge(5,1)
graph.print_adj_list()

