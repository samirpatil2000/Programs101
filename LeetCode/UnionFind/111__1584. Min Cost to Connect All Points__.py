from typing import List
class Solution:
    def findParent(self,parent:List[int],node):
        if node==parent[node]:
            return node
        parent[node]=self.findParent(parent,parent[node])
        return parent[node]
    def union(self,parent:List[int],u,v,rank):
        u_parent=self.findParent(parent,u)
        v_parent=self.findParent(parent,v)
        if rank[u_parent]<rank[v_parent]:
            parent[u_parent]=v_parent
        elif rank[u_parent]>rank[v_parent]:
            parent[v_parent]=u_parent
        else:
            rank[v_parent]+=1
            parent[u_parent]=v_parent
                    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result=0
        n=len(points)
        if n<=1:
            return 0
            
            
        parent=  [i for i in range(n)]
        rank  =  [0 for i in range(n)]
        def dis(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        es=[]
        for i in range(n):
            for j in range(n):
                if i != j:
                    es.append([i, j, dis(points[i], points[j])])
        
        es = sorted(es, key=lambda item: item[2])
        # print(es)
        i=0
        e=0
        while e < n and i<len(es):
            u, v, w =  es[i]
            
            u_parent=self.findParent(parent,u)
            v_parent=self.findParent(parent,v)
            i+=1
            if u_parent!=v_parent:
                result+=w
                e+=1
                self.union(parent,u_parent,v_parent,rank)
                
                
        return result
    
    
sol=Solution()
points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
print(sol.minCostConnectPoints(points))
        
        