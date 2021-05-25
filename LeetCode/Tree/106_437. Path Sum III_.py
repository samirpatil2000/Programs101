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

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        count_=[0]
        
        def dfs(root,tar=targetSum):
            if root==None:return
            if tar==0:
                count_[0]+=1
            if root.left:
                print(root.left.val,tar-root.left.val)
                if tar-root.left.val<0:
                    dfs(root.left)
                else:
                    dfs(root.left,tar-root.left.val)
            if root.right:

                print(root.right.val,tar-root.right.val)
                if tar-root.right.val<0:
                    dfs(root.right)
                else:
                    dfs(root.right,tar-root.right.val)
            return
        dfs(root)
        return count_[0]
    
    

sol=Solution()
data=[5,4,8,11,'*',13,4,7,2,'*','*',5,1]
targetSum = 22
root=sol.deserialize(data)
# sol.inOrder(root)
print(sol.pathSum(root,targetSum))
            