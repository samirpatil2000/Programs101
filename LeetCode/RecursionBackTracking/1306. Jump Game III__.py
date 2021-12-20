from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int,visited=set()) -> bool:
        
        if start<0 or start>=len(arr) or arr[start]==-1:
            return False
        if arr[start]==0:return True
        temp=arr[start]
        arr[start]=-1
        x=self.canReach(arr,start-temp) or self.canReach(arr,start+temp)
        return x

sol=Solution()
arr = [4,2,3,0,3,1,2]
start = 5
start = 0
arr = [3,0,2,1,2]
start = 2
print(sol.canReach(arr,start))
