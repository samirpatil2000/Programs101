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
    def isCompleteTree(self,root):
        q=collections.deque()
        q.append(root)
        last_stack_contains_star=False
        count=0
        while q:
            st=[]
            for _ in range(len(q)):
                temp=q.popleft()
                
                if temp.left:
                    if last_stack_contains_star:return False
                    q.append(temp.left)
                    if not st:
                        st.append(temp.left.val)
                    elif st[-1]!='*':
                        st.append(temp.left.val)
                    else:
                        return False
                else:
                    st.append('*')
                    count+=1
                if temp.right:
                    if last_stack_contains_star:return False
                    q.append(temp.right)
                    if not st:
                        st.append(temp.right.val)
                    elif st[-1]!='*':
                        st.append(temp.right.val)
                    else:
                        return False
                else:
                    st.append('*')
                    count+=1
                    
                if count>=1:
                    last_stack_contains_star=True
                
        return True
sol=Solution()
data=[1,2,3,4,5,6,7,8,9,10,11,12,13,'*','*',15]
root=sol.de(data)
print(sol.isCompleteTree(root))
