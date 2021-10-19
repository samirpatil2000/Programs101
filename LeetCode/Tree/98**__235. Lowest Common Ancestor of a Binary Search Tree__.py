import collections
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
    
    def de(self,data):
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
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'int', q: 'int') -> 'TreeNode':
        if not root:return
        if root.val>p and root.val>q:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val<p and root.val<q:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
        
            
    

    
    
sol=Solution()
data= [6,2,8,0,4,7,9,'*','*',3,5]
p = 7
q = 8
root=sol.de(data=data)
sol.inOrder(root)
print(sol.lowestCommonAncestor(root,p,q).val)