
class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inOrder(root):
    if(root==None):
        return
    print(root.val, end=" ")
    inOrder(root.left)
    inOrder(root.right)


def tree2str(t):
    if t==None:
        return ''
    str_=''
    str_+=str(t.val)
    if t.left==None and t.right==None:
        return str_
    # if t.left:
    str_+="("
    str_+=tree2str(t.left)
    str_+=")"
    if t.right:
        str_+=("("+tree2str(t.right)+")")
    return str_

root = newNode(1)

root.left=newNode(1)
root.left.right=newNode(1)
root.left.left=newNode(1)

root.right=newNode(1)
root.right.right=newNode(1)
root.right.left=newNode(1)

root.right.left.right=newNode(0)    

print(tree2str(root))
    
class Solution:
    def tree2str(self, t) -> str:
        def dfs(node):
            if not node:
                return ''
            res = ''
            res += str(node.val)
            
            if not node.left and not node.right:
                return res
            
            res += '('
            res += dfs(node.left)
            res += ')'
            
            right = dfs(node.right)
            if right:
                res += '('
                res += right
                res += ')'
            return res
        return dfs(t)
    