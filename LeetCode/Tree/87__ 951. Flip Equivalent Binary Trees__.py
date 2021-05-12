# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1==None and root2==None:
            return True
        if (root1 and root2==None) or (root2 and root1==None) or (root1.val!=root2.val):
            return False
        
        q1,q2=[root1],[root2]
        
        while(len(q1)>0):
            set_1,set_2={},{}
            if len(q1)!=len(q2):
                return False
            for _ in range(len(q1)):
                temp_1=q1.pop(0)
                temp_2=q2.pop(0)
                
                if temp_1.left:
                    set_1[temp_1.left.val]=temp_1.val
                    q1.append(temp_1.left)
                if temp_1.right:
                    set_1[temp_1.right.val]=temp_1.val
                    q1.append(temp_1.right)
                    
                if temp_2.left:
                    set_2[temp_2.left.val]=temp_2.val
                    q2.append(temp_2.left)
                if temp_2.right:
                    set_2[temp_2.right.val]=temp_2.val
                    q2.append(temp_2.right)
            if set_1!=set_2:
                return False
        return True
    

root=TreeNode(1)

root=TreeNode(1)