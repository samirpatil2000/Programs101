# https://leetcode.com/problems/maximum-binary-tree/



# Definition for a binary tree node.
class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root: newNode, target: int):
        list_=[]
        def nodeANDParentNode(root,parent_root):
            if root==None:
                return None
            
            nodeANDParentNode(root.left,root)
            nodeANDParentNode(root.right,root)
            if root.val==target and root.left==None and root.right==None:
                if parent_root:
                    if parent_root.left==root:
                        parent_root.left=None
                    elif parent_root.right==root:
                        parent_root.right=None
                else: 
                    return 
        nodeANDParentNode(root,None)
        if root.val==target and root.left==None and root.right==None:
            return None
        return root


def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)
    
    
root = newNode(2)

root.left=newNode(2)
# root.left.left=newNode(2)
root.right=newNode(2)
# root.right.left=newNode(2)
# root.right.right=newNode(4)
    
sol=Solution()
inOrder(root)
print()
inOrder(sol.removeLeafNodes(root,2))
print()
            

    
      

def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)


sol=Solution()
print()