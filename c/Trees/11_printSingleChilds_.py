
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



def printSingleChildNode(node,parent):
    if(node==None):
        return
    if(parent and parent.left==node and parent.right==None):
        print(node.data)
    elif(parent and parent.right==node and parent.left==None):
        print(node.data)
    printSingleChildNode(node.left,node)
    printSingleChildNode(node.right,node)
    
        
    



        

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
printSingleChildNode(root.left,root)
printSingleChildNode(root.right,root) 