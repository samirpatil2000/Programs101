from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deserialiazition(self,list_: List[int])->TreeNode:
        root=TreeNode(list_[0])
        q=[root]
        index=1
        while q:
            temp=q.pop(0)
            if index<len(list_) and list_[index]!='*':
                temp.left=TreeNode(list_[index])
                q.append(temp.left)
            index+=1
            if index<len(list_) and list_[index]!='*':
                temp.right=TreeNode(list_[index])
                q.append(temp.right)
            index+=1
                
        return root
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr=[]
        q=[root]
        
        while q:
            sum_=0
            for i in range(len(q)):
                temp=q.pop(0)
                sum_+=temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            arr.append(sum_)
        last_index=arr[0]
        slast_index=0
        res=arr[0]
        for i in range(1,len(arr)):
            temp=max(last_index,slast_index+arr[i])
            res=max(res,temp)
            slast_index=last_index
            last_index=temp
        return res
    
    def rob_II(self, root: Optional[TreeNode],memo={}) -> int:
    
        if not root:return 0
        if root in memo:
            return memo[root]
        val=0
        if root.left:
            val+=self.rob_II(root.left.right)+self.rob_II(root.left.left)
        if root.right:
            val+=self.rob_II(root.right.right)+self.rob_II(root.right.left)
        max_=max(val+root.val,self.rob_II(root.left)+self.rob_II(root.right))
        memo[root]=max_
        return max_
sol=Solution()
null='*'
data=root = [3,4,5,1,3,null,1]
data=root = [2,1,3,null,4]
root=sol.deserialiazition(data)
print(sol.rob(root))
print(sol.rob_II(root))