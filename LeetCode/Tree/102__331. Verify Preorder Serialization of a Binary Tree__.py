class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder=preorder.split(',')
        
        x=preorder.pop(0)
        if x=='#':return False
        
            
        root=TreeNode(val=x)
        q=[root]
        while q or root:
            if root:
                if len(preorder)==0:return True
                temp=preorder.pop(0)
                if temp!='#':
                    root.left=TreeNode(val=temp)
                    q.append(root.left)
                else:
                    root.left=None
                root=root.left
            else:
                root=q.pop(0)
                if len(preorder)==0:return False
                temp=preorder.pop(0)
                if temp!='#':
                    root.right=TreeNode(val=temp)
                    q.append(root.right)
                else:
                    root.right=None
                root=root.right
                
        if len(preorder)==0:return True
        return False

                
                
sol=Solution()
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
preorder = "1,#"
preorder = "9,#,#,1"
preorder = "1"
print(sol.isValidSerialization(preorder))