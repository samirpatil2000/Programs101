from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        def dfs(src):
            visited[src]=True
            for edge in rooms[src]:
                if visited[edge]==False:
                    dfs(edge)
        
        count=0
        for i in range(len(rooms)):
            if visited[i]==False:
                dfs(i)
                count+=1
        
        if count==1:
            return True
        return False
    

sol=Solution()
rooms=[[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))
                