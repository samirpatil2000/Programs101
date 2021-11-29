from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        redundant=None
        def findparent(node):
            if node==parent[node]:
                return node
            parent[node]=findparent(parent[node])
            return parent[node]
        def union(a,b):
            nonlocal redundant
            pa_a=findparent(a)
            pa_b=findparent(b)
            if pa_a==pa_b:
                redundant=[a,b]
            else:
                parent[pa_b]=pa_a
                
        for u,v in edges:union(u,v)
        return redundant
    
    
sol=Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection(edges))
        
            