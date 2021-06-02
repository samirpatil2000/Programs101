import collections
class Solution():
    def negativeWeightCycle(self,edges,n):
        dist=[1000000]*n
        for _ in range(n-1):
            for u,v,wt in edges:
                if dist[u]+ wt <dist[v]:
                    dist[v]=dist[u]+wt
        for u,v,wt in edges:
            if dist[u]+ wt <dist[v]:
                return True
        return False
    
    
sol=Solution()
n = 3
edges = [(0,1,-1),(1,2,-2),(2,0,3)]

print(sol.negativeWeightCycle(edges,n))
            
                        
        




