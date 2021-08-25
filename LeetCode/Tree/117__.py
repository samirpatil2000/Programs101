# Definition for a binary tree node.from easyBT.binarytree import BinaryTree,BinarySearchTree
from typing import NoReturn
from easyBT.binarytree import BinaryTree,BinarySearchTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchInBST(self,root:TreeNode,target,ex)->bool:
        if root:
            if root.val!=ex and root.val==target:
                return True
            else:
                if root.val>target:
                    return self.searchInBST(root.left,target,ex)
                if root.val<target:
                    return self.searchInBST(root.right,target,ex)
        return False
    def findTarget(self, root:TreeNode, k: int) -> bool:
        temp=root
        def findTarget_(root,k):
            if root:
                if self.searchInBST(temp,k-root.val,root.val)==True:
                    return True
                if findTarget_(root.left,k):
                    return True
                if findTarget_(root.right,k):
                    return True
            return False
        return findTarget_(root,k)
            
bt=BinarySearchTree()
null=None
root = [0,-1,2,-3,null,null,4]

k = -4
root=bt.DesializeTree(root)
sol=Solution()
print(sol.findTarget(root,k))
