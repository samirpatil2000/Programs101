"""
def change(x):
    x[0] = 3

x = [1]
change(x)
print(x)
"""




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
    
    
    
def constructTree(left,right,preorder,dict_):
    if left>right:
        return None
    root=newNode(preorder[constructTree.preIndex])
    index=dict_[preorder[constructTree.preIndex]]
    constructTree.preIndex +=1
    root.left=constructTree(left,index-1,preorder,dict_)
    root.right=constructTree(index+1,right,preorder,dict_) 
    return root
    
    
inorder=[3 ,1 ,4 ,0 ,5 ,2]
preorder = [0 ,1 ,3 ,4 ,2 ,5]
dict = {}
for i, e in enumerate(inorder):
    dict[e] = i
    
print(dict)


# static variable
constructTree.preIndex = 0
root=constructTree(0,len(inorder)-1,preorder,dict)

display(root)
inOrder(root)
print()
postOrder(root)














