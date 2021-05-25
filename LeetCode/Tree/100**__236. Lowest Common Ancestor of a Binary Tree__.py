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
    
    def lowestCommonAncestor_SPace(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        l_=[]
        def dfs(root,p,q,list_=[]):
            if root==None:return
            if root.val==p or root.val==q:
                l_.append(list_)
                if len(l_)>1:
                    return
            # x=list_.copy()
            # y=list_.copy()
            
            if root.left:
                # x.append(root.left.val)
                # print(x,root.left.val,"Before")
                dfs(root.left,p,q,list_+[root.left.val])
                # x.pop()
                # print(x,root.left.val,"After")
                # del x
            if root.right:
                # y.append(root.right.val)
                dfs(root.right,p,q,list_+[root.right.val])
                # del y
            # del list_
        dfs(root,p,q,[root.val])
        
        print(l_)
        i=0
        while (i<min(len(l_[0]),len(l_[1])) and l_[0][i]==l_[1][i]):
            i+=1
        return l_[0][i-1]
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parent={root:None}
        
        def dfs(root,p,q):
            if root==None:return
            if root.val==p or root.val==q:
                if p and q in parent:return
            if root.left:
                parent[root.left]=root
                dfs(root.left,p,q)
                
            if root.right:
                parent[root.right]=root
                dfs(root.right,p,q)
                
                
        dfs(root,p,q)
        accen=set()
        while p:
            accen.add(p)
            p=parent[p]
        while q and q not in accen:
            accen.add(q)
            q=parent[q]
        return q
        
        
        
                
                
                
            
    

    
    
sol=Solution()
data=[3,5,1,6,2,0,8,'*','*',7,4]
p = 5
q = 4
root=sol.de(data)
x=sol.lowestCommonAncestor(root,p,q)
print(x)
# y=sol.lowestCommonAncestor_SPace(root,p,q)
# print(y)