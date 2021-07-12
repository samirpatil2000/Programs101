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
    
    
    

root = newNode(10)
root.left=newNode(11)
root.right=newNode(7)
root.right.right=newNode(20)
root.right.left=newNode(2)
display(root)
        