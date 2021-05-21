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
    
    def verticalOrder_BFS(self,root):
        if not root:return
        queue=collections.deque()
        queue.append([root,0,0])
        dict_=collections.defaultdict(list)
        while queue:
            temp=queue.popleft()
            node,row,col=temp[0],temp[1],temp[2]
            dict_[col].append((row,node.val))
            if node.left:
                queue.append([node.left,row+1,col-1])
            if node.right:
                queue.append([node.right,row+1,col+1])
        
        result=[]
        for col in sorted(dict_.keys()):
            temp=[]
            for row in sorted(dict_[col]): #it will automatically sort according to your requirement
                temp.append(row[1])
                
            result.append(temp)
                 
        return result
    
            
    # def verticalOrder(self,root):
    #     # if not root:return
    #     # if root.left:
    #     def dfs(root,row,col):
    #         if not root:return
    #         if root.left:
    
            
    
sol=Solution()

data= [1,2,3,4,6,5,7]
x=sol.de(data)
print(sol.verticalOrder_BFS(x))
