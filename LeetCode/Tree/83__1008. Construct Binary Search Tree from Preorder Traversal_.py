# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binarySearch(self,arr,left,right,target):
        mid=(left+right)//2
        if arr[mid]==target:return mid
        if arr[mid]>target:return self.binarySearch(arr,left,mid-1,target)
        return self.binarySearch(arr,mid+1,right,target)
    
    def bstFromPreorder(self, preorder):
        inorder=preorder.copy()
        inorder.sort()
        preorder_index=[0]
        def helper(left,right):
            if left>right:
                return None
            root=TreeNode(preorder[preorder_index[0]])
            index=self.binarySearch(inorder,0,len(inorder)-1,preorder[preorder_index[0]])
            preorder_index[0]+=1
            root.left=helper(left,index-1)
            root.right=helper(index+1,right)
            return root
        return helper(0,len(preorder)-1)


def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.val,end=" ")
    inOrder(root.right)


sol=Solution()
preorder = [8,5,1,7,10,12]
x=sol.bstFromPreorder(preorder)
inOrder(x)
print()

        