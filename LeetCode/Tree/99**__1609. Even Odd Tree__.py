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
    def isEvenOddTree(self,root):
        q=collections.deque()
        q.append(root)
        level=1
        while q:
            min_=2**32
            max_=-2**32
            
            for _ in range(len(q)):
                print(min_,max_,level)
                print([i.val for i in q])
                temp=q.popleft()
                print(temp.val,end="  ")
                if temp.left:
                    # print(temp.left,"left")
                    if level%2==0:
                        if max_>=temp.left.val or temp.left.val%2!=level%2:
                            print("1")
                            return False
                        max_=temp.left.val
                    else:
                        if min_<=temp.left.val or temp.left.val%2!=level%2:
                            print("2")
                            return False
                        min_=temp.left.val     
                    q.append(temp.left)
                if temp.right:
                    if level%2==0:
                        if max_>=temp.right.val or temp.right.val%2!=0:
                            return False
                        max_=temp.right.val
                    else:
                        if min_<=temp.right.val or temp.right.val%2==0:
                            return False
                        min_=temp.right.val
                    q.append(temp.right)
            level+=1
            print()
        return True
    def isEvenOddTree_2(self, root: TreeNode) -> bool:
        level = 0
        curLevel = [root]
        nextLevel = []
        while curLevel: 
            for i in range(len(curLevel)): 
                cur = curLevel[i]
                if cur.left: 
                    nextLevel.append(cur.left)
                if cur.right: 
                    nextLevel.append(cur.right)
                if cur.val % 2 == level % 2: 
                    return False
                if i > 0 and level%2 == 0 and cur.val <= curLevel[i-1].val: 
                    return False
                if i > 0 and level%2 != 0 and cur.val >= curLevel[i-1].val: 
                    return False
            curLevel = nextLevel
            nextLevel = []
            level += 1
        return True
                        
                        
sol=Solution()
data= [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
root=sol.de(data)
print(sol.isEvenOddTree(root))
print(sol.isEvenOddTree_2(root))
                    
                
                