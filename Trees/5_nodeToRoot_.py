
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
    
def nodeToRoot(root,val,out):
    path=[]
    if(root == None):
        return False,[]
    if(root.data == val):
        path.append(root.data)
        print(out+","+str(root.data))
        return True,path
    if(root.left):
        findLeftChild,left_path=nodeToRoot(root.left,val,out+","+str(root.data))
        if(findLeftChild):
            path.append(root.data)
            path=path+left_path
            return True,path
    if(root.right):
        findRightChild,right_path=nodeToRoot(root.right,val,out+","+str(root.data))
        if(findRightChild):
            path.append(root.data)
            path=path+right_path
            return True,path
    return False,[]

def nodeToRoot_2(root,val):
    path=[]
    if(root == None):
        return False,[]
    if(root.data == val):
        path.append(root.data)
        return True,path
    if(root.left):
        findLeftChild,left_path=nodeToRoot_2(root.left,val)
        if(findLeftChild):
            path.append(root.data)
            path=path+left_path
            return True,path
    if(root.right):
        findRightChild,right_path=nodeToRoot_2(root.right,val)
        if(findRightChild):
            path.append(root.data)
            path=path+right_path
            return True,path
    return False,[]


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
    inOrder(root.left)
    
    inOrder(root.right)


root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(36)
root.left.left=newNode(12)
display(root)
inOrder(root)
print()
preOrder(root)

print()
w=nodeToRoot_2(root,70)
print(w)

"""
import os
my_file = 'my_file.txt'
base = os.path.splitext(my_file)[0]
os.rename(my_file, base + '.bin')
"""