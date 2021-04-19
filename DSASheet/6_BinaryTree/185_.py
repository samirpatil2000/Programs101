
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


def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

def postOrder(root):
    if root==None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
    
def postOrderIterative(root):
    st=[]
    out=[]
    curr=root
    while(len(st)>0 or curr):
        if(curr):
            st.append(curr)
            # if(curr.left):
            out.append(curr.data)
            curr=curr.right
                
        else:
            curr=st.pop()
            curr=curr.left
    out.reverse()
    print("\n",out)
    
    
def postOrderIterative_2(root):
    st=[root]
    out=[]
    while(len(st))>0:
        node=st.pop()
        out.append(node.data)
        if(node.left):
            st.append(node.left)
        if(node.right):
            st.append(node.right)
    out.reverse()
    print(out)
            
            
    

#using queue
# def postOrderIterative_3(root):
#     qu=[root]
#     out=[]
#     while(len(qu))>0:
#         node=qu.pop(0)
#         out.append(node.data)
#         if(node.right):
#             qu.append(node.right)
#         if(node.left):
#             qu.append(node.left)
        
#     out.reverse()
#     print(out)    
            
    
    
    


    
    
        

        

root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
root.left.left=newNode(12)


# root = newNode(5)
# root.left = newNode(3)
# root.right = newNode(6)
# root.left.left = newNode(2)
# root.left.left.right = newNode(1)
# root.left.right = newNode(4)
display(root)
inOrder(root)
print()
postOrder(root)
# print()
postOrderIterative(root)
postOrderIterative_2(root)
postOrderIterative_3(root)
print()