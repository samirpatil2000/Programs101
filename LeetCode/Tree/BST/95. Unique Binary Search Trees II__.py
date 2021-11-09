# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self,root:TreeNode)->List[int]:
        result=[]
        def in_order(root:TreeNode):
            if not root:
                return
            result.append(root.val)
            in_order(root.left)
            in_order(root.right)
        in_order(root)
        return result
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(left,right):
            if left>right:
                return [None]
            if left==right:
                return [TreeNode(val=left)]
            result=[]
            for i in range(left,right+1):
                left_roots=dfs(left,i-1)
                right_roots=dfs(i+1,right)
                for l in left_roots:
                    for r in right_roots:
                        result.append(TreeNode(val=i,left=l,right=r))
            return result
        return [self.inorder(r) for r in dfs(0,n)]

sol=Solution()
print(sol.generateTrees(5))
        


                        
                
        
        