# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrder(self,root):
        def d(root):
            if root==None:return
            d(root.left)
            print(root.val,end=" ")
            d(root.right)
        d(root)
        print()
        return
    def deserialiazition(self,list_: List[int])->TreeNode:
        root=TreeNode(list_[0])
        q=[root]
        index=1
        while q:
            temp=q.pop(0)
            if index<len(list_) and list_[index]!='*':
                temp.left=TreeNode(list_[index])
                q.append(temp.left)
            index+=1
            if index<len(list_) and list_[index]!='*':
                temp.right=TreeNode(list_[index])
                q.append(temp.right)
            index+=1
                
        return root
        
        
        
        
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder_index=0
        dict_={}
        for i,e in enumerate(inorder):
            dict_[e]=i
        def dfs(left,right):
            nonlocal preorder_index
            if left>right:
                return
            root=TreeNode(preorder[preorder_index])
            index=dict_[preorder[preorder_index]]
            preorder_index+=1
            root.left=dfs(left,index-1)
            root.right=dfs(index+1,right)
            return root
        return dfs(0,len(inorder)-1)
        
sol=Solution()
data= [6,2,8,0,4,7,9,'*','*',3,5]            

# root=sol.deserialiazition(data)

# sol.inOrder(root)

preorder = [-1]
inorder = [-1]
sol.inOrder(sol.buildTree(preorder,inorder))