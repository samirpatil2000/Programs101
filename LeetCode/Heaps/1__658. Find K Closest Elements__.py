from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q=[]
        for i in range(len(arr)):
            diff=abs(arr[i]-x)
            if len(q)<k:
                heapq.heappush(q,[-diff,arr[i]])
            else:
                temp=heapq.heappop(q)
                if -temp[0] > diff:
                    heapq.heappush(q,[-diff,arr[i]])
                    k-=1
                else:
                    heapq.heappush(q,[temp[0],temp[1]])
                    break
        print(q)
        result=[]
        for u,v in q:heapq.heappush(result,v)
        q=[]
        while result:q.append(heapq.heappop(result))
        return q
sol=Solution()
arr = [1,2,3,4,5]
k = 4
x = 3
arr = [1,1,1,10,10,10]
k =1
x = 9
print(sol.findClosestElements(arr,k,x))
        
        # left = 0
        # right = len(arr) - k
        
        # while left < right:
        #     mid = (left + right) >> 2
        #     mid_value = arr[mid]
            
        #     if x - arr[mid+k] <= mid_value - x:right = mid
        #     else:left = mid + 1
        
        # return arr[left : left + k]
    
# "username","otp","password","businessname","firstname","lastname","phone","email"