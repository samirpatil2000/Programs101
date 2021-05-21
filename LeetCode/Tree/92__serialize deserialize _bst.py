
from collections import deque
from typing import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Codec:

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
    
                
            

    def deserialize(self, data: str) -> TreeNode:
        # list_data=list(data.split(','))
        # print(list_data)
        # root=TreeNode(list_data.pop(0))
        # queue=[root]
        # while queue:
        #     temp=queue.pop(0)
        #     left_node=list_data.pop(0)
            
        #     if left_node!="*": # Use None instead of *
        #         temp.left=TreeNode(int(left_node))
        #         queue.append(temp.left)
                
        #     right_node=list_data.pop(0)
        #     if right_node!="*": # Use None instead of *
        #         temp.right=TreeNode(int(right_node))
        #         queue.append(temp.right)
                
        # return root
        if not data: return None
        tree = deque(data)
        root = TreeNode(int(tree.popleft()))
        queue = deque([root])
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
    
def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.val,end=" ")
    inOrder(root.right)
    
    
root = TreeNode(50)

root.left=TreeNode(25)
root.left.left=TreeNode(12)
root.left.right=TreeNode(37)
root.left.right.left=TreeNode(30)
root.left.right.right=TreeNode(40)

root.right=TreeNode(75)
root.right.right=TreeNode(87)
root.right.left=TreeNode(62)
root.right.left.right=TreeNode(70)
root.right.left.left=TreeNode(60)
inOrder(root)
print()
sol=Codec()
print(x:=sol.serialize(root))
x=[1,2,3,4,'*',2,4,'*','*',4]
inOrder(sol.deserialize(x))
print()