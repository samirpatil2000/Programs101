# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(root,depth):
            if root==None:
                return 0,None
            if root and root.left==None and root.right==None:
                return depth,root
            l_max_depth,l_cm_a=dfs(root.left,depth+1)
            r_max_depth,r_cm_a=dfs(root.right,depth+1)
            if l_max_depth==r_max_depth:
                return l_max_depth,root
            if l_max_depth>r_max_depth:
                return l_max_depth,l_cm_a
            else:
                return r_max_depth,r_cm_a
            
        return dfs(root,0)[1]
    
def inOrder(root):
    if root==None:return
    inOrder(root.left)
    print(root.val,end=" ")
    inOrder(root.right)
         
    
    
    
    
root=TreeNode(1)

root.left=TreeNode(2)
root.left.left=TreeNode(3)

root.left.left.right=TreeNode(6)

root.left.right=TreeNode(4)
root.left.right.right=TreeNode(5)
root.left.right.right.left=TreeNode(10)

# root.right=TreeNode(1)
# root.right.right=TreeNode(1)


sol=Solution()
inOrder(root)
print()
x=sol.lcaDeepestLeaves(root)
inOrder(x)
print()
