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
        # print()
        return
    
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
    def findDuplicateSubtrees(self, root: TreeNode):
        list_=[]
        dict_=collections.defaultdict(list)
        def duplicates(root):
            if root==None:return "null"
            str_ = "%s,%s,%s" % (str(root.val), duplicates(root.left), duplicates(root.right))
            dict_[str_].append(root.val)
            return str_
        
        duplicates(root)
        for str_ in dict_.keys():
            if len(dict_[str_])>1:
                list_.append(dict_[str_][0])
            
        return list_
            
data=[1,2,3,4,'*',2,4,'*','*',4]
sol=Solution()
x=sol.de(data)
sol.inOrder(x)
print()
y=sol.findDuplicateSubtrees(x)
print(y)

