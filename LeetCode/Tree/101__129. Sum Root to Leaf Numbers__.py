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
        tree = collections.deque(data.split(","))
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
    
    def sumNumbers(self, root: TreeNode) -> int:
        sum_=[0]
        def dfs(root,ssf):
            if root==None:return
            if root and root.left==None and root.right==None:
                print(ssf)
                sum_[0]+=int(ssf)
                return
            if root.left:
                dfs(root.left,ssf+str(root.left.val))
            if root.right:
                dfs(root.right,ssf+str(root.right.val))
        dfs(root,str(root.val))
        return sum_[0]
    
    def pathSum(self, root: TreeNode, targetSum: int):
        if root==None:return []
        list_=[]
        def dfs(root,psf,ssf):
            if root==None:return
            if root and root.left==None and root.right==None:
                x=[int(i) for i in psf.split(",")]
                if targetSum==ssf:
                    print(psf)
                    list_.append(x)
                return
            if root.left:
                dfs(root.left,psf+","+str(root.left.val),ssf+root.left.val)
            if root.right:
                dfs(root.right,psf+","+str(root.right.val),ssf+root.right.val)
        dfs(root,str(root.val),root.val)
        return list_
    def zigzagLevelOrder(self, root: TreeNode):
        q=[root]
        level=1
        list_=[]
        while q:
            l=collections.deque()
            for _ in range(len(q)):
                temp=q.pop(0)
                if temp.left:
                    q.append(temp.left)
                    if level%2==0:
                        l.appendleft(root.left.val)
                    else:
                        l.append(root.left.val)
                    
                        
                if temp.right:
                    q.append(temp.right)
                    if level%2==0:
                        l.appendleft(root.right.val)
                    else:
                        l.append(root.right.val)
            level+=1
        return list_
    
sol=Solution()
data=[5,4,8,11,'*',13,4,7,2,'*','*',5,1]
targetSum = 22
root=sol.deserialize(data)
print(x:=sol.serialize(root))
print(X)
# print(sol.sumNumbers(root))
print(sol.pathSum(root,targetSum))