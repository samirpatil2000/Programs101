# Definition for a binary tree node.
from typing import NoReturn


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        if root and root.left==None and root.right==None:
            return root
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root