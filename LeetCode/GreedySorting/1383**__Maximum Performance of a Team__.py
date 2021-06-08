from typing import List
import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr=zip(efficiency,speed)
        arr=sorted(arr)
        
        teamSum=0
        max_performance=0
        selectedTeam=[]
        for i in range(n-1,-1,-1):
            heapq.heappush(selectedTeam,arr[i][1])
            teamSum+=arr[i][1]
            if len(selectedTeam)>k:
                
                teamSum-=heapq.heappop(selectedTeam)
            max_performance=max(max_performance,teamSum*arr[i][0])
            
        return max_performance
            
            


n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

sol=Solution()
print(sol.maxPerformance(n,speed,efficiency,k))