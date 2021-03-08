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

graph_.add_edge(0,1,10)
graph_.add_edge(2,3,10)
graph_.add_edge(4,5,10)
graph_.add_edge(5,6,10)
graph_.add_edge(4,6,10)
graph_.print_graph()





def getConnectedComp(graph,src,visited,compo_list):
    visited[src]=True
    compo_list.append(src)
    for _ in range(graph.get_nbr(src)):
        temp=graph.get_node(src)
        while(temp):
            if(visited[temp.nbr]==False):
                getConnectedComp(graph,temp.nbr,visited,compo_list)   
            temp=temp.next
    return
    

    
visited=[False for _ in range(v+1)]
tree_s=[]  
for i in range(v+1):
    if(visited[i]==False):
        compo_list=[]
        getConnectedComp(graph_,i,visited,compo_list)
        # print(compo_list)
        tree_s.append(compo_list)
print(tree_s)