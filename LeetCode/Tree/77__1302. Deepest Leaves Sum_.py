# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_height=[0]
        dict_=defaultdict(list)
        def fun(root,current_height):
            if root==None:
                return
            if root and root.left==None and root.right==None:
                # print(root.val)
                if current_height>=max_height[0]:
                    max_height[0]=current_height
                    temp=dict_[current_height]
                    dict_.clear()
                    
                    dict_[current_height].append(root.val)
                    dict_[current_height]+=temp
                return
            if root.left:
                fun(root.left,current_height+1)
            if root.right:
                fun(root.right,current_height+1)
        fun(root,0)
        sum_=0
        for i in dict_.values():
            sum_+=sum(i)
                # sum_+=sum(j)
        return sum_
    

root=TreeNode(1)

root.left=TreeNode(2)
root.left.right=TreeNode(5)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(7)

root.right=TreeNode(3)
root.right.right=TreeNode(6)
root.right.right.right=TreeNode(8)


sol=Solution()
print(sol.deepestLeavesSum(root))