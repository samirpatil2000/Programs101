class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: TreeNode):
        def findDepth(root):
            if root==None:return 0
            return max(findDepth(root.left),findDepth(root.right))+1
        h=findDepth(root)
        col=h
        width=2*h-1
        mat=[[""]*width for _ in range(col)]
        print(mat)
        
        def dfs(root,row,col):
            if row>=len(mat) or col<0:return
            if root==None:return
            mat[row][col]=str(root.val)
            dfs(root.left,row+1,col-1)
            dfs(root.right,row+1,col+1)
        dfs(root,0,col//2)
            
        
        
        print(mat)
    
root=TreeNode(3)

root.left=TreeNode(5)
# root.left.left=TreeNode(6)
# root.left.right=TreeNode(2)
# root.left.right.left=TreeNode(7)
# root.left.right.right=TreeNode(4)

# root.right=TreeNode(1)
# root.right.right=TreeNode(8)
# root.right.left=TreeNode(0)



sol=Solution()

sol.printTree(root)
            