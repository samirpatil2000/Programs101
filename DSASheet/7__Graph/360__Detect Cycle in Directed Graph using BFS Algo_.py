from collections import defaultdict
import collections
from typing import Counter

class Graph:
    
    def __init__(self,vertices):
        self.graph={}
        self.vertices=vertices+1
    
        for i in range(self.vertices):
            self.graph[i]=[]
        
    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def printGraph(self):
        for i in self.graph.keys():
            print(i,"->",self.graph[i])
            
    def topologicalSort_DFS(self):
        visited=[False for _ in range(len(self.graph.keys()))]
        st=[]
        def dfs(src):
            visited[src]=True
            for i in self.graph[src]:
                if visited[i]==False:
                    dfs(i)
            st.append(src)
        for i in self.graph.keys():
            if visited[i]==False:
                dfs(i)
        st.reverse()
        return st
    def topoBFS(self,numCourses):
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
 


g=Graph(3)
# g.add_edge(0,1)
# g.add_edge(1,2)
# g.add_edge(0,2)
# g.add_edge(2,0)
# g.add_edge(2,3)


g.add_edge(1,0)

g.add_edge(3,0)

g.add_edge(3,2)
g.add_edge(2,1)
# g.printGraph()
visited=[False for _ in range(g.vertices)]

# print(visited,in_curr)/
print("Topo DFS ",g.topologicalSort_DFS())
print(g.topoBFS())
        