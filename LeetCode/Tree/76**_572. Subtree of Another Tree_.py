# Definition for a binary tree node.
# https://leetcode.com/problems/subtree-of-another-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    #     if not s or not t:
    #         return False
    #     def check(n1,n2):
    #         if not n1 and not n2:
    #             return True
    #         elif not n1 or not n2 or n1.val!=n2.val:
    #             return False
    #         else:
    #             return check(n1.left,n2.left) and check(n1.right,n2.right)
    #     return check(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)    
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        nodes=[]
        def returnNodeWithRep(root,val):
            if root==None:
                return None
            if root.val==val:
                nodes.append(root)
            returnNodeWithRep(root.left,val)
            returnNodeWithRep(root.right,val)
            
        def isEqualFunction(rootA,rootB):
            if rootA==None and rootB==None:
                return True
            if rootA and rootB and rootA.val==rootB.val:
                if isEqualFunction(rootA.left,rootB.left) and isEqualFunction(rootA.right,rootB.right):
                    return True
            return False
        returnNodeWithRep(root,subRoot.val)
        # print(nodes)
        for node in nodes:
            if isEqualFunction(node,subRoot):
                return True
        return False