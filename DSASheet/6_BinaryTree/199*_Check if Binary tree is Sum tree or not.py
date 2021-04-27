# https://practice.geeksforgeeks.org/problems/sum-tree/1




class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class ListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


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
    if root==None:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)
    
    
def isSumTree(root):
    
    if root and root.left==None and root.right==None:
        return True
    
    if root and root.left and root.right==None:
        return False
    elif root and root.left==None and root.right:
        return False
    
    if root.data!=root.left.data+root.right.data:
        return False
    if isSumTree(root.left) and isSumTree(root.right):
        return True
    return False
        
    


root = TreeNode(50)

root.left=TreeNode(20)
root.left.left=TreeNode(10)
root.left.right=TreeNode(10)

root.right=TreeNode(30)
root.right.right=TreeNode(10)
root.right.left=TreeNode(20)



inOrder(root)
print()
print(isSumTree(root))





    