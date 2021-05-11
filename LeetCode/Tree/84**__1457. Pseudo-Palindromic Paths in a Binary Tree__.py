# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def is_palindrome(self,arr):
        odd_count=0
        for i in range(10):
            if arr[i]!=0:
                print(arr[i],i)
                if arr[i]%2!=0 and odd_count==1:
                    return False
                if arr[i]%2!=0 and odd_count==0:
                    odd_count+=1
        return True
    def pseudoPalindromicPaths (self, root):
        list_=[0 for _ in range(10)]
        count=[0]
        path_=""
        def dfs(root,list_,path_):
            
            if root==None:
                return
            
            if root and root.left==None and root.right==None:
                list_[root.val]+=1
                print(list_,path_+str(root.val))
                if self.is_palindrome(list_):
                    count[0]+=1
                return
            list_[root.val]+=1
            x=list_.copy()
            if root.left:
                dfs(root.left,list_,path_+str(root.val))
            if root.right:
                # print(root.val ,list_)
                
                dfs(root.right,x,path_+str(root.val))
    
        dfs(root,list_,path_)
        return count[0]
    
    
    
    
root=TreeNode(2)

root.left=TreeNode(3)
root.left.left=TreeNode(3)
root.left.right=TreeNode(1)

root.right=TreeNode(1)
root.right.right=TreeNode(1)


sol=Solution()
# print(sol.pseudoPalindromicPaths(root))
arr=[0,0,0,0,3,0,0,0,2,1]
print(sol.is_palindrome(arr))

# [8,6,9,null,null,null,4,4,1,5,4,null,null,null,null,8]