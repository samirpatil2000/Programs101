
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
    
    
def iterativePrePostInOrder(root):
    st=[]
    inOrder=[]
    preOrder=[]
    postOrder=[]
    st.append([root,1])
    while(len(st)>0):
        temp=st[len(st)-1]
        if(temp[1]==1):
            preOrder.append(temp[0].data)
            temp[1]+=1
            
            if(temp[0].left):
                st.append([temp[0].left,1])
                
        elif(temp[1]==2):
            inOrder.append(temp[0].data)
            temp[1]+=1
            if(temp[0].right):
                st.append([temp[0].right,1])
        else:
            postOrder.append(temp[0].data)
            st.pop()
        # print(st)
            
    print(inOrder)
    print(preOrder)
    print(postOrder)
        
            
            
def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)
    
def preOrder(root):
    if(root==None):
        return
    print(root.data,end=" ")
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if(root==None):
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
        

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
preOrder(root)
print()
inOrder(root)
print()
postOrder(root)
print()


iterativePrePostInOrder(root)