# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def display(head):
    left_node=0.0
    right_node=0.0
    if not head:
        return
    if(head.left):
        left_node=head.left.data
    if(head.right):
        right_node=head.right.data
    print(left_node,"<-",head.data,"->",right_node)
    display(head.right)
    display(head.left)
        
            
            
def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


def isUnivalTree(root):
    print("s")
    if root==None:
        return True
    
    if root and root.left and  root.right:
        if root.data!=root.left.data or root.left.data!=root.right.data:
            return False
    elif root and root.left:
        if root.data!=root.left.data:
            return False
    elif root and root.right:
        if root.data!=root.right.data:
            return False    
    if isUnivalTree(root.left) and isUnivalTree(root.right):
        return True
    return False
    
    
    
        

root = newNode(1)

root.left=newNode(1)
root.left.right=newNode(1)
root.left.left=newNode(1)

root.right=newNode(1)
root.right.right=newNode(1)
root.right.left=newNode(1)

root.right.left.right=newNode(0)

inOrder(root)
print()

print(isUnivalTree(root))

    
   
    