from collections import Counter
from typing import List
import math
class Union:
    def __init__(self,n:int) -> None:
        self.parent=list(range(n))
    def findParent(self,u):
        if self.parent[u]==u:
            return u
        self.parent[u]=self.findParent(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        parent_u=self.findParent(u)
        parent_v=self.findParent(v)
        self.parent[parent_v]=self.parent[parent_u]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_=max(nums)
        uf=Union(max_+1)
        for num in nums:
            for j in range(2,int(math.sqrt(num)+1)):
                if num%j==0:
                    uf.union(num,j)
                    uf.union(num,num//j)
                    
        counter = Counter([uf.findParent(num) for num in nums])
        return max(counter.values())
        dict_={}
        print(uf.parent)
        for i in nums:
            temp=uf.parent[i]
            dict_[temp]=dict_.get(temp,0)+1
            
        return max(dict_.values()),dict_


sol=Solution()
nums = [2,3,6,7,4,12,21,39]
# nums = [20,50,9,63]
# nums=[100,68,70,79,80,20,25,27]
print(sol.largestComponentSize(nums))

        