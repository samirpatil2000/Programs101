

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

        

root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(98)
root.right.left=newNode(62)
# root.right.left.right=newNode(70)
root.left.right=newNode(37)
# root.left.right.left=newNode(36)
root.left.left=newNode(12)
display(root)
inOrder(root)
print()


def makeAlist(root,list_):
    if(root==None):
        return
    if(root.left):
        makeAlist(root.left,list_)
    list_.append(root.data)
    if(root.right):
        makeAlist(root.right,list_)    
        
def makeRightTiltTree(root):
    list_=[]
    makeAlist(root,list_)    
    root=newNode(list_[0])
    temp=root
    i=1
    while(i<len(list_)):
        temp.right=newNode(list_[i])
        temp.left=None
        temp=temp.right
        i+=1
    return root
        
        
        
        
    
    


# x=makeRightTiltTree(root)
# display(x)


def inOrderApproach(curr,node):
    if(node==None):
        return
    # if(node.left):
    inOrderApproach(curr,node.left)
    node.left=None
    curr.right=node
    curr=node
    # if(node.right):
    inOrderApproach(curr,node.right)
    
def optimiseApproach(root):
    curr=newNode(0)
    temp=curr
    inOrderApproach(curr,root)
    return temp

y=optimiseApproach(root)
display(y)
print("Ts ")
display(root)
    
    
    
    
    
    