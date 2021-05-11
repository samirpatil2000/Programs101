# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root==None:
            count_=[]
            return 0
        count_=[1]
        max_=root.val
        
        def helperFun(root,max_):
            
            if root==None:
                return
            max_=max(max_,root.val)
            if root.left:
                if root.left.val>=max_:
                    count_[0]+=1
                helperFun(root.left,max_)
                
            if root.right:
                if root.right.val>=max_:
                    count_[0]+=1
                helperFun(root.right,max_)
        helperFun(root,max_)
        return count_[0]