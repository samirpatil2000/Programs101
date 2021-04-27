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

def invertTree(root):
    if root==None or (root.left==None and root.right==None):
        return
    r_x=root.right
    root.right=root.left
    root.left=r_x
    invertTree(root.left)
    invertTree(root.right)
    
    
    
        

root = newNode(50)

root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)

root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)







inOrder(root)
print()


    
   
    