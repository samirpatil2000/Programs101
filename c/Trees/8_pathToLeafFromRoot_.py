
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


def pathToLeafFromRoot(root,output,sum):
    if(root==None):
        return
    if(root.left == None and root.right ==None):
        print(output+str(root.data),"Sum = ",sum+root.data)
        return
    if(root.left):
        pathToLeafFromRoot(root.left,output+str(root.data)+",",sum+root.data)
    if(root.right):
        pathToLeafFromRoot(root.right,output+str(root.data)+",",sum+root.data)
    return

        
            
        

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

# display(root)
pathToLeafFromRoot(root," ",0)
