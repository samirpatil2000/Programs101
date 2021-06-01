import collections
from typing import List
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
    
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i=0
        self.result=[]
        def dfs(root):
            if root==None:return
            if root.val!=voyage[self.i]:
                self.result.append(-1)
                return
            if self.i < len(voyage) and root.left and root.left.val!=voyage[self.i]:
                self.result.append(root.val)
                dfs(root.right)
                dfs(root.left)
            else:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        for j in range(len(self.result)):
            if self.result[j]==-1:
                return [-1]
        return self.result
    
    
sol=Solution()
data= [8,9,4,12,46,7,14,48,29,6,37,10,'*','*',15,26,3,50,42,45,'*',17,40,'*','*',18,'*','*',25,11,31,41,'*','*','*',1,'*','*','*',22,19,'*','*','*','*',13,'*','*','*','*',34,'*','*',27,'*',23,'*',28,38,'*','*',33,'*',16,20,'*','*',43,'*',44,35,5,49,21,36,24,'*',2,47,'*','*','*','*','*',39,'*','*','*','*','*','*','*',32,'*',30]
voyage=[8,9,12,29,42,50,41,34,48,26,25,49,31,11,13,38,43,24,28,46,6,45,1,37,40,22,27,33,44,47,30,2,32,35,19,23,16,5,3,39,20,36,21,17,4,14,15,18,7,10]
root=sol.deserialize(data)
print(sol.flipMatchVoyage(root,voyage))
        
                        
