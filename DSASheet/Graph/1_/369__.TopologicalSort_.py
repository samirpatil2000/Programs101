class Graph:
    def __init__(self,vertices) -> None:
        
        self.graph={}
        self.v=vertices+1
        
        for i in range(self.v):
            self.graph[i]=[]
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
            
            
    def topologicalSort(self):
        visited=[False for _ in range(self.v)]
        st=[]
        def dfs(src):
            visited[src]=True
            for i in self.graph[src]:
                if visited[i]==False:
                    dfs(i)
            st.append(src)
        for i in range(self.v):
            if visited[i]==False:
                dfs(i)
        st.reverse()
        return st
            
    
    
g=Graph(6)
g.add_edge(0,3)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(5,6)

g.printGraph()

print(g.topologicalSort())