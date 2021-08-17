
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node',visited=set()) -> 'Node':
        if node==None:
            return None
        if node and len(node.neighbors)==0:
            return Node(node.val)
        
        visited={}
        def dfs(node):
            visited[node]=Node(node.val)
            new_node_neighbors=[]
            for e in node.neighbors:
                if e not in visited:
                    dfs(e)
                new_node_neighbors.append(visited[e])
            visited[node].neighbors=new_node_neighbors
        dfs(node)
        return visited[node]
        
            