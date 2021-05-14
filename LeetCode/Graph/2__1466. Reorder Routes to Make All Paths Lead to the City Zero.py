from collections import defaultdict
class Solution:
    def minReorder(self, n, connections):
        graph=defaultdict(set)
        count_=0
        
        for edge in connections:
            graph[edge[0]].add(edge[1])
        add_connections=set()
        
        print([graph[i] for i in range(n)])
        def detectConnectionToZero(src):
            if src==0 or src in add_connections:
                return True
            for i in graph[src]:
                if detectConnectionToZero(i):
                    return True
            add_connections.add(src)
            return False
        
        for i in range(1,n):
            if detectConnectionToZero(i)==False:
                count_+=1
        print(add_connections)
        return count_,len(add_connections)
    
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = 5
connections = [[1,0],[1,2],[3,2],[3,4]]

n = 3
connections = [[1,0],[2,0]]
sol=Solution()
print(sol.minReorder(n,connections))