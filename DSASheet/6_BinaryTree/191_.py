
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
    
def height(root):
    if root==None:
        return -1
    return max(height(root.left),height(root.right))+1

    

def checkIsBalanced(root):
    left_height=height(root.left)
    right_height=height(root.right)
    
    return left_height-right_height
    

    
    
            
            
            
            
    

    
    



# root = newNode(50)
# root.left=newNode(25)
# root.right=newNode(75)
# root.right.right=newNode(87)
# root.right.left=newNode(62)
# root.right.left.right=newNode(70)
# root.left.right=newNode(37)
# root.left.right.left=newNode(36)
# root.left.left=newNode(12)

root=newNode(10)
root.left=newNode(20)
root.left.left=newNode(40)
root.left.right=newNode(50)
# root.right=newNode(30)
display(root)

print(checkIsBalanced(root))
