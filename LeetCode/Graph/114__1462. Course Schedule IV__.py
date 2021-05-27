from typing import List
import collections
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph={}
        for i in range(numCourses):graph[i]=set()
        for u,v in prerequisites:graph[u].add(v)
        
        def dfs(src,visited,to_find):
            visited.add(src)
            if to_find in graph[src]:
                return True
            for edge in graph[src]:
                if edge not in visited:
                   if dfs(edge,visited,to_find):return True
            return False
        result=[]
        for q1,q2 in queries:
            visited=set()
            # visited.add(q2)
            if dfs(q1,visited,q2):
                result.append(True)
            else:
                result.append(False)
        return result
    
sol=Solution()
numCourses = 3
prerequisites =  [[1,2],[1,0],[2,0]]
queries =[[1,0],[1,2]]
print(sol.checkIfPrerequisite(numCourses,prerequisites,queries))