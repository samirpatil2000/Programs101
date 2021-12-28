from typing import List
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph=collections.defaultdict(list)
        self.result=collections.deque()
        self.indegrees=[0]*numCourses
        for u,v in prerequisites:
            self.graph[u].append(v)
        for src in range(numCourses):
            for edge in self.graph[src]:
                self.indegrees[edge]+=1
        q=[]
        for i in range(numCourses):
            if self.indegrees[i]==0:
                q.append(i)
        while q:
            temp=q.pop()
            self.result.appendleft(temp)
            for edge in self.graph[temp]:
                self.indegrees[edge]-=1
                if self.indegrees[edge]==0:
                    q.append(edge)
            
        for i in range(numCourses):
            if self.indegrees[i]!=0:
                return []
        return self.result
    
    
    
    
    
    
sol=Solution()
numCourses = 2
prerequisites = [[0,1],[1,0]]
print(sol.findOrder(numCourses,prerequisites))
             
            