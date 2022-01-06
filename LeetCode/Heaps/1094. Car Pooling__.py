from sys import path
from typing import List


from heapq import heappush,heappop,heapify
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        queue=[]
        for i,u,v in trips:
            heappush(queue,[u,i])
            heappush(queue,[v,-i])
        # print(queue)
        while queue:
            u,v=heappop(queue)
            capacity-=v
            if capacity<0:
                return False
        return True
            
                
            
        
        
sol=Solution()
trips = [[2,1,5],[3,3,7]]
capacity = 5
print(sol.carPooling(trips,capacity))
v=sorted([x for n, i, j in trips for x in [[i, n], [j, - n]]])
print(v)      