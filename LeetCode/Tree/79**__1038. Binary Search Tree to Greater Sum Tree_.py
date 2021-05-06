# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


# Definition for a binary tree node.
class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def bstToGst(self, root: newNode):
        sum_=[0]
        def fun(root):
            if root==None:
                return
            fun(root.right)
            sum_[0]+=root.val
            root.val=sum_[0]
            fun(root.left)
        fun(root)
        return root



def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)

def postOrder(root):
    if(root==None):
        return
    postOrder(root.right)
    print(root.val, end=" ")
    postOrder(root.left)
    
    
root = newNode(4)

root.left=newNode(1)
root.left.right=newNode(2)
root.left.right.right=newNode(3)
root.left.left=newNode(0)


root.right=newNode(6)
root.right.left=newNode(5)
root.right.right=newNode(7)
root.right.right.right=newNode(8)




sol=Solution()
inOrder(root)
print()
# postOrder(root)
inOrder(sol.bstToGst(root))
print()