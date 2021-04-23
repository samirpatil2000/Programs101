

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


def mergeBothTheTrees(root1,root2):
    if root1 and root2:
        mergeRoot=newNode(root1.data+root2.data)
        mergeRoot.left=mergeBothTheTrees(root1.left,root2.left)
        mergeRoot.right=mergeBothTheTrees(root1.right,root2.right)
        return mergeRoot
    if root1==None:
        return root2
    elif root2==None:
        return root1
        
    
    
        

root_1 = newNode(50)
root_1.left=newNode(25)
root_1.right=newNode(75)
root_1.right.right=newNode(98)
root_1.right.left=newNode(62)
root_1.right.left.right=newNode(70)
root_1.left.right=newNode(37)
root_1.left.right.left=newNode(36)
root_1.left.left=newNode(12)



root_2 = newNode(50)
root_2.left=newNode(25)
root_2.right=newNode(75)
root_2.right.right=newNode(98)
root_2.right.left=newNode(62)
inOrder(root_1)
print()
inOrder(root_2)
print()
x=mergeBothTheTrees(root_1,root_2)
inOrder(x)






    
    
    
    
    
    