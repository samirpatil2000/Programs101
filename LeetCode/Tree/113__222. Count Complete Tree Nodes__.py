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
    
    def deserialize(self,data):
        if not data: return None
        tree = collections.deque(data)
        root = TreeNode(int(tree.popleft()))
        queue = collections.deque([root])
        while queue:
            Treenode = queue.popleft()
            if tree:
                if (left_Treenode := tree.popleft()) != '*':
                    Treenode.left = TreeNode(int(left_Treenode))
                    queue.append(Treenode.left)
            if tree:
                if (right_Treenode := tree.popleft()) != '*':
                    Treenode.right = TreeNode(int(right_Treenode))
                    queue.append(Treenode.right)
                
        return root
    
    def countNodes(self,root):
        if root==None:return 0
        def leftDepth(root):
            if root==None:return 0
            d=0
            while root:
                d+=1
                root=root.left
            return d
        def rightDepth(root):
            if root==None:return 0
            d=0
            while root:
                d+=1
                root=root.right
            return d
        ld=leftDepth(root.left)
        rd=rightDepth(root.right)
        
        if ld==rd:
            return 2**(ld+1)-1
        return 1 + self.countNodes(root.left)+self.countNodes(root.right)
sol=Solution()
data= [1,2,3,4,5,6]

root=sol.deserialize(data)

print(sol.countNodes(root))

    
        