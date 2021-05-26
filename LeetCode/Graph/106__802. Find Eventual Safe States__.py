from typing import Counter, List
import collections
class Solution:
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited=[False]*len(graph)
        in_curr_dfs=[False]*len(graph)
        def detectCycle(src):
            visited[src]=True
            in_curr_dfs[src]=True
            
            for edge in graph[src]:
                if visited[edge]==False:
                    if detectCycle(edge):
                        return True
                elif in_curr_dfs[edge]:
                    print(in_curr_dfs)
                    return True
            in_curr_dfs[src]=False
            return False
        result=[]
        for i in range(len(graph)):
            if visited[i]==False:
                detectCycle(i)
        print(in_curr_dfs)

        for i in range(len(in_curr_dfs)):
            if in_curr_dfs[i]==False:
                result.append(i)                 
        return result
    
        
sol=Solution()
graph= [[],[0,2,3,4],[3],[4],[]]
graph= [[0],[1,2,3,4],[1,3,4],[2,4],[2]]
print(sol.eventualSafeNodes(graph))
            
            