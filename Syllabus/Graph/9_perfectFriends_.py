import sys
from sys import stdin, stdout

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
"""
n = int(stdin.readline())
graph_=Graph(n)

i=5
while(i>0):
    
    arr = [x for x in stdin.readline().split()]
    v1,v2=int(arr[0]),int(arr[1])
    graph_.add_edge(v1,v2,10)
    i-=1
# 6
# 0 1
# 2 3
# 4 5
# 5 6
# 4 6
"""   
v=6
graph_=Graph(v)   
graph_.add_edge(0,1,10)
graph_.add_edge(2,3,10)
graph_.add_edge(4,5,10)
graph_.add_edge(5,6,10)
graph_.add_edge(4,6,10)
graph_.print_graph()



visited=[False for i in range(v+1)]
def perfectFriends(graph,vertices,visited):
    trees=[]
    for i in range(vertices):
        if(visited[i]==False):
            compo_list=[]
            drawTreeComp(graph,i,visited,compo_list)
            trees.append(compo_list)
    return trees
    
    
def drawTreeComp(graph,src,visited,compo_list):
    visited[src]=True
    compo_list.append(src)
    temp=graph.get_node(src)
    while(temp):
        if(visited[temp.nbr]==False):
            drawTreeComp(graph,temp.nbr,visited,compo_list)
        temp=temp.next


x=perfectFriends(graph_,v,visited)

print(x)
total=0
for i in range(len(x)):
    for j in range(i+1,len(x)):
        total+=(len(x[i])*len(x[j]))

print(total)


