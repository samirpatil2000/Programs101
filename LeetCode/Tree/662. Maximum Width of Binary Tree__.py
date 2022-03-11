
# Definition for a binary tree node.
from collections import deque
from typing import Optional

from easyBT.binarytree import BinaryTree, BinarySearchTree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        level = [(root, 0)]
        while level:
          new_level = []
          ans = max(ans, level[-1][1] - level[0][1] + 1)
          for node, pos in level:
            if node.left:
              new_level.append((node.left, pos * 2))
            if node.right:
              new_level.append((node.right, pos * 2 + 1))
              
          level = new_level
        return ans
    
bt = BinarySearchTree()
null = None
root = [1,3,2,5,3,null,9]
root = [1,3,null,5,3]
root = [1,null,3]
# root = [1,3,1,5,null,null,9,6,null,null,7]

root = bt.DesializeTree(root)
sol = Solution()
print(sol.widthOfBinaryTree(root))
