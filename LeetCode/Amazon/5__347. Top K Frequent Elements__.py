from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_={}
        for i in nums:
            if i not in dict_:
                dict_[i]=0
                
            dict_[i]+=1
        queue=[]
        for idx in dict_.keys():
            heapq.heappush(queue,[-dict_[idx],idx])
        dict_=[]
        for _ in range(k):
            res=heapq.heappop(queue)
            dict_.append(res[1])
        return dict_
        
sol=Solution()
nums=[1,1,1,2,2,3]
k=2
nums = [1]
k = 1
print(sol.topKFrequent(nums,k))
            
        
x=(4,)+(5,)
print(x)