from collections import defaultdict 

class Solution():
    def __init__(self,connections,n) -> None:
        self.graph=defaultdict(list)
        self.vertices=n+1
                
        for edge in connections:
            self.graph[edge[0]].append(edge[1])
        print([self.graph[i] for i in range(self.vertices)])
    
    def topoBFS(self):
        numCourses=self.vertices
        indegree={}
        visited={}
        for i in range(numCourses):
            indegree[i]=0
            visited[i]=False
        for i in range(numCourses):
            for j in self.graph[i]:
                indegree[j]+=1
        queue=[]
        count_=0
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            temp=queue.pop(0)
            visited[temp]=True
            count_+=1
            for e in self.graph[temp]:
                if visited[e]==False:
                    indegree[e]-=1
                    if indegree[e]==0:
                        queue.append(e)
        if count_==numCourses:
            return True
        return False

             
            
            
                    
    
    
n,connections=6,[[0,3],[0,1],[1,2],[2,3],[4,3],[4,5],[4,6],[5,6]]
# n,connections=3,[[1,0],[2,3],[2,1],[0,2],[3,1]]

sol=Solution(connections,n)
print(sol.topoBFS())
