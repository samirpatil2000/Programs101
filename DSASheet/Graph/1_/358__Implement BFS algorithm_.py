

class Graph:
    def __init__(self,vertices) -> None:
        self.graph={}
        self.v=vertices+1
        
        for i in range(self.v):
            self.graph[i]=[]
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def printGraph(self):
        for i in range(self.v):
            print(i,"->",self.graph[i])

graph=Graph(4)
graph.add_edge(2,4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,3)

# print(graph.v)
# print(graph.graph[0])
# graph.printGraph()

def bfs(graph,src):
    visited=[False for _ in range(graph.v)]
    queue=[src]
    while(len(queue)>0):
        temp=queue.pop(0)
        print(temp,end=" ")
        if visited[temp]==True:
            continue
        visited[temp]=True
        # print(graph.graph[temp])
        for i in graph.graph[temp]:
            if visited[i]==False:
                queue.append(i)
    print()
        
bfs(graph,0)