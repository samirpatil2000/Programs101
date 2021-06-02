import collections

class Node:
    def __init__(self,u,v,wt) -> None:
        self.u=u;
        self.v=v;
        self.wt=wt;

def makeGraph(list_,N):
    graph=collections.defaultdict(list)
    for l in list_:
        graph[l[0]].append(Node(l[0],l[1],l[2]))
    return graph
    
    
      

def bellmanFord(list_,src,N):
    graph=makeGraph(list_)
    dist=[10000000]*N;
    dist[src]=0;
    for i in range(0,N):
        for edge in graph:
            if dist[edge.u]+edge.wt<dist[edge.v]:
                dist[edge.v]=dist[edge.u]+edge.wt
    for edge in graph:
        if dist[edge.u]+edge.wt<dist[edge.v]:
            print("Negative cycle")
    return dist
            
        
    
        
    
     