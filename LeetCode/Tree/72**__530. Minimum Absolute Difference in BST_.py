# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inOrder(root):
    if(root==None):
        return
    print(root.val, end=" ")
    inOrder(root.left)
    inOrder(root.right)
    
# def getMinDiff(root):
#     if root==None:
#         return 2**32
#     if root and root.left==None and root.right==None:
#         return 2**32
    
    
#     l_min,r_min=2**32,2**32
#     self_l,self_r=2**32,2**32
#     if root.left:
#         self_l=abs(root.val - root.left.val)
#     if root.right:
#         self_r=abs(root.val - root.right.val)
        
#     if root.left:
#         l_min=getMinDiff(root.left)
#     if root.right:
#         r_min=getMinDiff(root.right)
#     print(self_l,self_r,l_min,r_min)
#     return min(l_min,r_min,min(self_l,self_r))

# res=sys.maxsize


def getMinDiif(root):
    if root==None:
        return
    if root.left:
        getMinDiif(root.left)
        
    if getMinDiif.previous!=-1:
        getMinDiif.res=min(getMinDiif.res,abs(root.val-getMinDiif.previous))
    getMinDiif.previous=root.val
    
    if root.right:
        getMinDiif(root.right)   




root = TreeNode(236)

root.left=TreeNode(104)
# root.left.left=TreeNode(701)
root.left.right=TreeNode(227)
# root.left.right.left=TreeNode(20)

root.right=TreeNode(701)
# root.right.right=TreeNode(10)
root.right.left=TreeNode(911)


getMinDiif.res=sys.maxsize
getMinDiif.previous=-1
print(getMinDiif(root))
print(getMinDiif.res)

# [236,104,701,null,227,null,911]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = sys.maxsize
        last_val = []

        def helper(root):
            nonlocal res
            if root.left: 
                helper(root.left)
            if last_val: 
                res = min(res, abs(root.val - last_val.pop()))
            last_val.append(root.val)
            if root.right: 
                helper(root.right)
        helper(root)

        return res
sol=Solution()
print(sol.getMinimumDifference(root))

