import collections 
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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
    def serialize(self, root: Node) -> str:
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
        root = Node(int(tree.popleft()))
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if tree:
                if (left_node := tree.popleft()) != '*':
                    node.left = Node(int(left_node))
                    queue.append(node.left)
            if tree:
                if (right_node := tree.popleft()) != '*':
                    node.right = Node(int(right_node))
                    queue.append(node.right)
                
        return root
    
    def connect(self, root: 'Node') -> 'Node':
        q=collections.deque()
        q.append[root]
        while q:
            temp=root
            for i in range(len(q)):
                node=q.popleft()
                if i==0:
                    temp=node
                    # =temp.next
                else:
                    temp.next=node
                    temp=temp.next
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return root
    
    def connectUsingDFS(self, root: 'Node') -> 'Node':
        dict_={}
        def dfs(root,level):
            if root==None:
                return
            root.next=dict_[level]
            dict_[level]=root
            dfs(root.right,level+1)  
            dfs(root.left,level+1)
        dfs(root)
        return root
    def connect1(self, root):
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
    
            
                


sol=Solution()
data= [1,2,3,4,5,6,7]

root=sol.deserialize(data) 