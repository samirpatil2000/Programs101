# https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1




class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class ListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


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

def dupTree(root,dict_):
    if root==None:
        return "$"
    # str_=""
    if root.left==None and root.right==None:
        str_=str(root.data)
        return str_
    str_=str(root.data)
    str_+=dupTree(root.left,dict_)
    str_+=dupTree(root.right,dict_)
    
    
    # if len(str_)>1:
    if str_ not in dict_:
        dict_[str_]=0
    dict_[str_]+=1
    return str_
        
     

    
    
    
    


root = TreeNode(5)

root.left=TreeNode(3)
root.left.left=TreeNode(1)
root.left.right=TreeNode(2)
# root.left.right.left=TreeNode(20)

root.right=TreeNode(3)
root.right.right=TreeNode(2)
root.right.left=TreeNode(1)



inOrder(root)
print()
dict_={}
print(dupTree(root,dict_))
print(dict_)



    