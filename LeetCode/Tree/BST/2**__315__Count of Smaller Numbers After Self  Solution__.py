from typing import List


class Node:
    def __init__(self,val,left=None,right=None,leftSubTreeSize=0) -> None:
        self.val=val
        self.left=left
        self.right=right
        self.leftSubTreeSize=leftSubTreeSize
        
class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # list_=[0]*n
        # for i in range(n-1,-1,-1):
        #     count_=0
        #     for j in range(i+1,n):
        #         if nums[i]>nums[j]:
        #             count_+=1
                    
        #     list_[i]=count_
        # return list_
        if not nums:return []
        if len(nums)==1:return [0]
        n=len(nums)
        result=[0]*n
        j=1
        while(j<n and nums[j-1]<=nums[j]):
            j+=1
        if(j==n):
            return result
        
        j=n-2
        while(j>-1 and nums[j]>=nums[j+1]):
            if(nums[j]>nums[j+1]):
                result[j]=n-j-1;
            if(nums[j]==nums[j+1]):
                result[j]=result[j+1]
            j-=1
        
        if j==-1:return result
        
        
        
        result=[0]
        
        def makeATree(node,val,numberOfSmallElement):
            if not node:
                node=Node(val)
                result.append(numberOfSmallElement)
                return node
            else:
                if val>node.val:
                    node.right=makeATree(node.right,val,numberOfSmallElement+1+node.leftSubTreeSize)
                elif val==node.val:
                    node.right=makeATree(node.right,val,numberOfSmallElement+node.leftSubTreeSize)
                else:
                    node.leftSubTreeSize+=1
                    node.left=makeATree(node.left,val,numberOfSmallElement)
                return node        
        
        root=Node(nums[-1])
        
        for i in range(n-2,-1,-1):
            makeATree(root,nums[i],0)
        return result[::-1]