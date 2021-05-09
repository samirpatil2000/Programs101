# Definition for a binary tree node.
from typing import NoReturn



# DP


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n):
        # n_=[n]
        def helper(n):
            if n==0:
                return None
            root=TreeNode(0)
            n-=1
            root.left=helper(n//2)
            root.right=helper(n//2)
            return root
        return helper(n)
        
            
    def inOrder(self,root):
        if root==None:
            return
        print(root.val,end=" ")
        self.inOrder(root.left)
        self.inOrder(root.right)
    

sol=Solution()
sol.inOrder(sol.allPossibleFBT(7))
print()