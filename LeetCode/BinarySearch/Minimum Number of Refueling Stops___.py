from typing import List
import heapq
class Solution:
    # def binarySearch(self,arr,left,right,target):
    #     if left>right:
    #         return -1
    #     mid=(left+right)//2
    #     if arr[mid][0]==target:
    #         return mid
    #     if (arr[mid][0]<target):
    #         if mid+1<len(arr) and arr[mid+1][0]>target:
    #             return mid
    #         elif mid+1>=len(arr):
    #             return mid
    #         else:
    #             return self.binarySearch(arr,mid+1,right,target)
    #     else:
    #         return self.binarySearch(arr,left,mid-1,target)
            

    # def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
    #     if len(stations)==0:
    #         if target<=startFuel:
    #             return 0
    #         else:
    #             return -1
                
    #     i=startFuel
    #     count_=0
        
    #     while i<target:
    #         x=self.binarySearch(stations,0,len(stations)-1,i)
    #         # print("i",i,"x",x)
    #         if x==-1:return -1
    #         i-=stations[x][0]
    #         target-=stations[x][0]
    #         i+=stations[x][1]
    #         count_+=1
    #     return count_
    
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q=[]
        xCurrenPos=startFuel
        stops=0
        heapq.heapify(q)
        for point,fuel in stations:
            while xCurrenPos<point:
                if q:
                    x=heapq.heappop(q)
                    xCurrenPos+=-x
                    stops+=1
                else:
                    return -1
            heapq.heappush(q,-fuel)
        
        while xCurrenPos<target:
            if q:
                x=heapq.heappop(q)
                xCurrenPos+=-x
                stops+=1
            else:
                return -1
        return stops
    
    
sol=Solution()
target = 100
startFuel = 50
stations =[[25,50],[50,25]]
print(sol.minRefuelStops(target,startFuel,stations))
            
        