# https://www.geeksforgeeks.org/print-paths-root-specified-sum-binary-tree/




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

list_=[]
def pathFromRootUpto_k_sum(root,psf,ssf,k,list_):
    
    if root==None:
        return
    print(psf)
    if k==ssf:
        list_.append(psf)
        return
    
    if root.left:
        pathFromRootUpto_k_sum(root.left,psf+" "+str(root.left.data),ssf+root.left.data,k,list_)
    if root.right:
        pathFromRootUpto_k_sum(root.right,psf+" "+str(root.right.data),ssf+root.right.data,k,list_)
    

        
    
    
    

    
    
    
    


root = TreeNode(10)

root.left=TreeNode(28)


root.right=TreeNode(13)
root.right.left=TreeNode(14)
root.right.left.left=TreeNode(21)
root.right.left.right=TreeNode(22)
root.right.right=TreeNode(15)
root.right.right.left=TreeNode(23)
root.right.right.right=TreeNode(24)


inOrder(root)
print()
k=38
print(pathFromRootUpto_k_sum(root,str(root.data),root.data,k,list_))

print(list_)
    