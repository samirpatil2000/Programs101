import collections
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inOrder(self,root):
        def in_order(root):
            if root==None:return
            in_order(root.left)
            print(root.val,end=" ")
            in_order(root.right)
        in_order(root)
        print()
        return
    def serialize(self, root: TreeNode) -> str:
        if not root: return ''
        queue=[root]
        str_=""
        while queue:
            temp=queue.pop(0)
            if temp:
                str_+=str(temp.val)
                queue.extend([temp.left,temp.right])
                str_+=","
            else:
                str_+="*"
                str_+=","
        return str_[:-1]
    
    def deserialize(self,data):
        if not data: return None
        tree = collections.deque(data)
        root = TreeNode(int(tree.popleft()))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if tree:
                if (left_node := tree.popleft()) != '*':
                    node.left = TreeNode(int(left_node))
                    queue.append(node.left)
            if tree:
                if (right_node := tree.popleft()) != '*':
                    node.right = TreeNode(int(right_node))
                    queue.append(node.right)
                
        return root

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root==[]:
            return 0
        count_=[0]
        
        def dfs(root,list_:List[int]):
            if root==None:return
            count_[0]+=list_.count(targetSum)
            if root.left:
                dfs(root.left,[x+root.left.val for x in list_]+[root.left.val])
            if root.right:
                dfs(root.right,[x+root.right.val for x in list_]+[root.right.val])
        dfs(root,[root.val])
        return count_[0]
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result=[]
        def dfs(root,list_so_far,sum_):
            if root and root.left==None and root.right==None:
                if sum_==targetSum:
                    result.append(list_so_far)
                return 
            if root.left:dfs(root.left,list_so_far+[root.left.val],sum_+root.left.val)
            if root.right:dfs(root.right,list_so_far+[root.right.val],sum_+root.right.val)
            
                
        dfs(root,[root.val],root.val)
        return result
            
    
    
    

sol=Solution()
# data = [10,5,-3,3,2,'*',11,3,-2,'*',1]
# targetSum = 8
# root=sol.deserialize(data)
# # sol.inOrder(root)
# print(sol.pathSum(root,targetSum))
root=[5,4,8,11,'*',13,4,7,2,'*','*',5,1]
targetSum = 22
root = [1,2,3]
targetSum = 5
root=sol.deserialize(root)
print(sol.pathSum(root,targetSum))
