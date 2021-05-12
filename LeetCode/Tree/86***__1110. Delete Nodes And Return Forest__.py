# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

class Solution:
    def inOrder(self,root):
        list_=[]
        def in_order(root):
            if root==None:return
            in_order(root.left)
            list_.append(root.val)
            print(root.val,end=" ")
            in_order(root.right)
        in_order(root)
        print()
        return list_
    def delNodes(self, root, to_delete):
        delete_set=set(to_delete)
        result=[]
        def walk(root,is_parent_exist):
            if root==None:return None
            if root.val in delete_set:
                root.left=walk(root.left,is_parent_exist=False)
                root.right=walk(root.right,is_parent_exist=False)
                return None
            else:
                if not is_parent_exist:
                    result.append(root)
                root.left=walk(root.left,is_parent_exist=True)
                root.right=walk(root.right,is_parent_exist=True)
                return root
        walk(root,False)
            
        return [self.inOrder(i) for i in result]
    

root=TreeNode(1)

root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

root.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)


sol=Solution()
to_delete = [3,5]
print(sol.delNodes(root,to_delete))