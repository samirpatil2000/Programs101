
from typing import List
from easyBT.binarytree import BinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sortedArrayToBST(nums:List[int]):
    if len(nums)==0:return None
    mid=len(nums)//2
    return TreeNode(val=nums[mid],left=sortedArrayToBST(nums[:mid]),right=sortedArrayToBST(nums[mid+1:]))
    


def h(root):
    if root==None:
        return -1
    return max(h(root.left),h(root.right))+1     
            
def inOrder(root):
    if(root==None):
        return
    print(root.val, end=" ")
    inOrder(root.left)
    inOrder(root.right)
    
    
# nums =[0,1,2,3,4,5]
nums=[-10,-3,0,5,9]
bt=BinaryTree()
root=sortedArrayToBST(nums)
# print((bt.InOrderTraversal(root)))
print(bt.SerializeTree(root))  
    