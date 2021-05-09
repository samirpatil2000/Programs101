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
visited={}

# list_=[]
# clonedGraph(g.graph,visited,1,list_)
# print(list_)

class Solution:
    def cloneGraph(self, graph,node: 'Node') -> 'Node':
        visited={}
        first_node=[None]
        def clonedGraph(graph,src_node):
            print("test :1:",src_node.val)
            visited[src_node.val]=1
            cloned=Node(src_node.val)
            for i in src_node.neighbors:
                if i not in visited:
                    clonedGraph(graph,graph.graph[i])    
                cloned.neighbors.append(i)
            if first_node[0]!=None:
                first_node[0]=cloned
        clonedGraph(graph,node)
        return first_node[0]
    
sol=Solution()
print(g.return_first_node().val)
sol.cloneGraph(g,g.return_first_node())
    
    




"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
"""
class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        # if there no node
        if not node:
            return node

        visited = {}
        
        # store the first node class address reference 
        # with new clone node address
        visited[node] = Node(node.val)
        
        self.dfs(node, visited)
        # print(visited)
        # print(visited[node.neighbors[0]].val)
        
        return visited[node]
        
    
    def dfs(self, node, visited):
        
        # traverse to the old node's neighnors node class address 
        for neighbor in node.neighbors:
            
            # if old node neighbors node class address not in the map key
            if neighbor not in visited:
                
                # here we store the old node class address as a key with reference
                # clone node class address value 
                visited[neighbor] = Node(neighbor.val)
                
                # going next edge
                self.dfs(neighbor, visited)
            
            # here we store the clone node class address with it's
            # new clone neighbor's class address 
            visited[node].neighbors.append(visited[neighbor])
     