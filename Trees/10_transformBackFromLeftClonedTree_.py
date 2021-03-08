
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




def createLeftClone(root):
    if(root==None):
        return None
    lcr=createLeftClone(root.left)
    rcr=createLeftClone(root.right)
    new_node=newNode(root.data)
    new_node.left=lcr
    root.right=rcr
    root.left=new_node
    return root


def TransfromFromLeftCloneTree(root):
    if(root==None):
        return None
    lcr=TransfromFromLeftCloneTree(root.left.left)
    rcr=TransfromFromLeftCloneTree(root.right)
    root.right=rcr
    root.left=lcr
    return root



        

root = newNode(50)
root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)
print("Main Tree")
display(root)
print("Left Cloned Tree")
createLeftClone(root)
display(root)
print("Main Tree")
TransfromFromLeftCloneTree(root)
display(root)