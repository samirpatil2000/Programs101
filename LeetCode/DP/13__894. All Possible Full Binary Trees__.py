# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        
        def dfs(n,list_=[0,0,0]):
            if n==1:
                print(list_)
                return
            dfs(n-2,list_+[0,0])
            dfs(n-2,list_+[None,None,0,0])
        dfs(n)
        
sol=Solution()
n=7
sol.allPossibleFBT(n)