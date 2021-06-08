from typing import List

class Node:
    def __init__(self,num):
        self.val=num
        self.parent=self
        self.size=1
    
class Union:
    def findParent(self,node):
        if node!=node.parent:
            return self.findParent(self,node.parent)
        return node.parent
    def union(self,node_1,node_2):
        parent_1=self.findParent(node_1)
        parent_2=self.findParent(node_2)
        if parent_1!=parent_2:
            parent_2.parent=parent_1
            parent_1.size+=parent_2.size
        return parent_1.size
        
        
class Solution:
    def longestConsecutive_2(self, nums: List[int]) -> int:
        nums=set(nums)
        count_=0
        for num in nums:
            if num-1 not in nums:
                #nums-1 is our starting point
                next_num=num+1
                while next_num in nums:
                    next_num+=1
                count_=max(count_,next_num-num)
        return count_
    
    def longestConsecutive(self, nums: List[int]) -> int:
        uf=Union()
        nums=set(nums)
        nodes={}
        result=0
        for num in nums:
            if num not in nodes:
                node=Node(num)
                nodes[num]=node
                size=0
                if num+1 in nodes:
                    size=uf.union(node,nodes[num+1])
                if num-1 in nodes:
                    size=uf.union(node,nodes[num-1])
                result=max(result,size)
        return result
    


sol=Solution()
nums =  [0,3,7,2,5,8,4,6,0,1]
print(sol.longestConsecutive(nums))
print(sol.longestConsecutive_2(nums))