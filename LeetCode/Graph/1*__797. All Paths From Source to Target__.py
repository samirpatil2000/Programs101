class Solution:
    def allPathsSourceTarget(self, graph):
        k
        
    
        def dfsBottomUp(src=0):    
            if src == len(graph) - 1: 
                return [[len(graph) - 1]]
            # return [([src] + path) for i in graph[src] for path in dfsBottomUp(i)]
            result=[]
            for e in graph[src]:
                for path in dfsBottomUp(e):
                    result.append([src]+path)
            return result
        
        return compo_list,dfsBottomUp()
    
graph = [[1,2],[3],[3],[]]
sol=Solution()
print(sol.allPathsSourceTarget(graph))