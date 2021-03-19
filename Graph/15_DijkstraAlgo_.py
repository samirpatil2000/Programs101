

import queue
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



class PriorityQueue:
    
    def __init__(self):
        self.queue=[]
        
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self): 
        return len(self.queue) == 0
    
    def insert(self, data): 
        self.queue.append(data) 
        
    def pop(self): 
        try: 
            min_ = 0
            for i in range(len(self.queue)): 
                if self.queue[i][2] < self.queue[min_][2]: 
                    min_ = i 
            item = self.queue[min_]
            del(self.queue[min_])
            return item 
        except IndexError: 
            print() 
            exit() 
            

v=6
graph_=Graph(v)   
graph_.add_edge(0,3,20)
graph_.add_edge(0,1,10)
graph_.add_edge(1,2,10)
graph_.add_edge(2,3,10)
graph_.add_edge(3,4,3)
graph_.add_edge(4,6,8)
# graph_.add_edge(2,5,10)
graph_.add_edge(4,5,3)
graph_.add_edge(5,6,3)
graph_.print_graph()


def djkstraAlgo(graph,src,visited):
    queue_=PriorityQueue() 
    queue_.insert([src,str(src)+"",0])
    while(not queue_.isEmpty()):
        rem=queue_.pop()
        if(visited[rem[0]]==True):
            continue
        visited[rem[0]]=True
        print(rem[0],"--",rem[1],"@",rem[2])
        edge_=graph.get_node(rem[0])
        while(edge_):
            if(visited[edge_.nbr]==False):
                queue_.insert([edge_.nbr,rem[1]+str(edge_.nbr),rem[2]+edge_.wt])
            edge_=edge_.next
    

visited=[False for _ in range(v+1)]
djkstraAlgo(graph_,0,visited)
    
