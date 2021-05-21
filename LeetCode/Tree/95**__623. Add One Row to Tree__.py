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
    
    def addOneRow_BFS(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        #showing error
        q=collections.deque()
        q.append(root)
        count_=depth
        while q:
            x=len(q)
            for _ in range(x):
                temp=q.popleft()
                # print(temp.val)
                # if count_==1:
                #     temp.left=TreeNode(val,temp)
                if count_==2:
                    temp.left=TreeNode(val,temp.left)
                    temp.right=TreeNode(val,temp.right)
                
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            count_-=1
            
            
        return root
    def addOneRow_DFS(self,root,val,depth):
        if root==None or depth<=0:return None
        if depth==1:
            return TreeNode(val,left=root)
        if depth==2:
            root.left=TreeNode(val,left=root.left)
            root.right=TreeNode(val,right=root.right)
        else:
            root.left=self.addOneRow_DFS(root.left,val,depth-1)
            root.right=self.addOneRow_DFS(root.right,val,depth-1)
        return root
        
    
    
sol=Solution()
data=[4,2,6,3,1,5]
val=1
depth=2
root=sol.de(data)
root2=sol.de(data)

x=sol.addOneRow_BFS(root,val,depth)
x2=sol.addOneRow_DFS(root2,val,depth)
# sol.inOrder(x)
print(sol.serialize(x))
print(sol.serialize(x2))

    
                        
                        
            
    
    