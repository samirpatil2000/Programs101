from typing import Union
class Union_(object):
    def __init__(self,n) -> None:
        self.parent=list(range(n))
    def findParent(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findParent(self.parent[node])
        return self.parent[node]
    def union(self,a,b):
        parent_a=self.findParent(a)
        parent_b=self.findParent(b)
        if parent_a!=parent_b:
            self.parent[parent_a]=parent_b
        
    def printParent(self):
        print(self.parent)
        

class Solution(object):
    
    
    def findCircleNumUsingDFS(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if not M: return 0
        s = len(M)
        seen = set()
        
        def dfs(p):
            for q, adj in enumerate(M[p]):
                print(M[p])
                print(q,adj,p)
                if (adj == 1) and (q not in seen):
                    seen.add(q)
                    dfs(q)
        cnt = 0
        for i in range(s):
            if i not in seen: 
                dfs(i)
                cnt += 1
        return cnt
    def findCircleNumUnionFind(self,isConnected):
        if not isConnected:return 0
        parent=Union_(len(isConnected))
        parent.printParent()
        for row in range(len(isConnected)):
            for col in range(row,len(isConnected[0])):
                if isConnected[row][col]==1:
                    parent.union(row,col)
        return len(set([parent.findParent(i) for i in range(len(isConnected))]))
        
        
    
    
    
sol=Solution()
isConnected = [[1,1,0],
               [1,1,0],
               [0,0,1]]
# print(sol.findCircleNumUsingDFS(isConnected))
print(sol.findCircleNumUnionFind(isConnected))