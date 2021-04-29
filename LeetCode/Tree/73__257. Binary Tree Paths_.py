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


root = TreeNode(236)

# root.left=TreeNode(104)
# # root.left.left=TreeNode(701)
# root.left.right=TreeNode(227)
# # root.left.right.left=TreeNode(20)

# root.right=TreeNode(701)
# # root.right.right=TreeNode(10)
# root.right.left=TreeNode(911)



class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = sys.maxsize
        list_ = []

        def helper(root,out_so_far):
            if root and root.left==None and root.right==None:
                list_.append(out_so_far)
                return
            if root.left: 
                helper(root.left,out_so_far+"->"+str(root.left.val))
            if root.right: 
                helper(root.right,out_so_far+"->"+str(root.right.val))
        helper(root,str(root.val))

        return list_
sol=Solution()
print(sol.getMinimumDifference(root))


