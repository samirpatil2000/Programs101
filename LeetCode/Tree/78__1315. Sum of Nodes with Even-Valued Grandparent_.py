# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_=[0]
        def fun(root):
            if root==None:
                return
            if (root.left and (root.left.left or root.left.right)) or (root.right and (root.right.left or root.right.right)):
                if root.val%2==0:
                    
                    if root.left:
                        l=root.left
                        if (l.left):
                            sum_[0]+=l.left.val
                        if (l.right):
                            sum_[0]+=l.right.val
                            
                    if root.right:
                        r=root.right
                        if (r.left):
                            sum_[0]+=r.left.val
                        if (r.right):
                            sum_[0]+=r.right.val        
                        
            fun(root.left)
            fun(root.right)
            
        fun(root)
        return sum_[0]

root=TreeNode(1)

root.left=TreeNode(2)
root.left.right=TreeNode(5)
root.left.left=TreeNode(4)
root.left.left.left=TreeNode(7)

root.right=TreeNode(3)
root.right.right=TreeNode(6)
root.right.right.right=TreeNode(8)


sol=Solution()
print(sol.sumEvenGrandparent(root))