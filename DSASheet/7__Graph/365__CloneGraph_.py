class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Graph:
    def __init__(self,vertices) -> None:
        self.v=vertices+1
        self.graph=[Node() for _ in range(self.v)]
        
        
        self.graph[0+1]=Node(1,[2, 4])
        self.graph[1+1]=Node(2,[1, 3])
        self.graph[2+1]=Node(3,[2, 4])
        self.graph[3+1]=Node(4,[1, 3])
    
    def return_first_node(self):
        return self.graph[1]
        
        
    def printGraph(self,node_val):
        queue=[node_val]
        visited=[False for _ in range(5)]
        list_=[]
        while(len(queue)):
            # print(queue)
            temp=queue.pop(0)
            if visited[temp]==True:
                continue
            
            visited[temp]=True
            # print(temp)
            for i in self.graph[temp].neighbors:
                if visited[i]==False:
                    queue.append(i)
            list_.append(self.graph[temp].neighbors)
        print(list_)
                
                
        
        # for i in self.graph:
        #     print(i.val,"->",i.neighbors)
        # print([i.neighbors for i in self.graph])
        
        
def clonedGraph(graph,visited,src_node_val,list_):
    visited[src_node_val]=1
    cloned=Node(src_node_val)
    for i in graph[src_node_val].neighbors:
        if i not in visited:
            clonedGraph(graph,visited,i,list_)    
        cloned.neighbors.append(i)
    list_.append(cloned.neighbors)
    

    
    

g = Graph(4)

g.printGraph(1)    




"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        if node and len(node.neighbors)==0:
            return Node(node.val)
        visited={}
        
        def dsf(node,visited):
            visited[node]=Node(node.val)
            
            for n in node.neighbors:
                if n not in visited:
                    dfs(n,visited)
                visited[node].neighbors.append(visited[n])
        
        dsf(node,visited)
        return visited[node]
     