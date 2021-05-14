from collections import defaultdict 

class Solution():
    def __init__(self,connections,n) -> None:
        self.graph=defaultdict(list)
        self.vertices=n+1
                
        for edge in connections:
            self.graph[edge[0]].append(edge[1])
        print([self.graph[i] for i in range(self.vertices)])
    
    def topoDFS(self):
        visited=[False for _ in range(self.vertices)]
        st=[]
        def is_dfs_topo(src,parent):
            visited[src]=True
            
            for i in self.graph[src]:
                if visited[i]==False:
                    if is_dfs_topo(i,src):
                        return True
                elif parent!=i:
                    return True
            st.append(src)  
            return False       
            
        for i in self.graph.keys():
            if visited[i]==False:
                if is_dfs_topo(i,None):
                    return st,True

        return st,True

             
            
            
                    
    
    
n,connections=6,[[0,3],[0,1],[1,2],[2,3],[4,3],[4,5],[4,6],[5,6]]
# n,connections=3,[[1,0],[2,3],[2,1],[0,2],[3,1]]

sol=Solution(connections,n)
print(sol.topoDFS())
