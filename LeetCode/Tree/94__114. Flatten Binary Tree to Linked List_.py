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
    def flatten(self, root: TreeNode) -> None:
        
        def dfs(root):
            if root==None:
                return
            if root and root.left==root.right:
                return root
            x,y=None,None
            if root.left:
                x=dfs(root.left)
            if root.right:
                y=dfs(root.right)
            root.left=None
            root.right=x
            
            if x:
                prev=x
                while(x.right):
                    print("x")
                    prev=x
                    x=x.right
                x.right=y
                    
            else:
                root.right=y
                
            return root
        
        self.inOrder(root)
        print()
        x=dfs(root)
        self.inOrder(x)
        
        
            
    
sol=Solution()
x=sol.de(data=[1,2,5,3,4,'*',6])
sol.flatten(x)

