# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


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

    
    
        

root = newNode(1)

root.left=newNode(0)
root.left.right=newNode(1)
root.left.left=newNode(0)

root.right=newNode(1)
root.right.right=newNode(1)
root.right.left=newNode(0)

    
    

def sumRootToLeaf(root,o_s_f,list_):
    if root and root.left==None and root.right==None:
        list_.append(int(o_s_f,2))
        sumRootToLeaf.sum_+=int(o_s_f,2)
        return
    
    if root.left:
        sumRootToLeaf(root.left,o_s_f+str(root.left.data),list_)
    if root.right:
        sumRootToLeaf(root.right,o_s_f+str(root.right.data),list_)
    

_list_=[]
sumRootToLeaf.sum_=0
sumRootToLeaf(root,str(root.data),_list_)
print(_list_,sumRootToLeaf.sum_)
# _list_=[int(i,2) for i in _list_]
# print(_list_,sum(_list_))
    
    
   
    