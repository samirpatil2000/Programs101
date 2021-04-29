import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = sys.maxsize
        last_val = -1

        def helper(root):
            nonlocal res
            nonlocal last_val
            if root.left: 
                helper(root.left)
            if last_val!=-1: 
                res = min(res, abs(root.val - last_val))
            last_val=root.val
            if root.right: 
                helper(root.right)
        helper(root)

        return res
    



root = TreeNode(236)

root.left=TreeNode(104)
# root.left.left=TreeNode(701)
root.left.right=TreeNode(227)
# root.left.right.left=TreeNode(20)

root.right=TreeNode(701)
# root.right.right=TreeNode(10)
root.right.left=TreeNode(911)



sol=Solution()
print(sol.getMinimumDifference(root))