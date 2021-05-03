# https://www.geeksforgeeks.org/find-largest-subtree-sum-tree/




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

def largetSumTree(root):
    if root==None:
        return 0,0
    l_sum,l_max=largetSumTree(root.left)
    r_sum,r_max=largetSumTree(root.right)
    self_sum=l_sum+r_sum+root.data 
    return self_sum,max(self_sum,l_max,r_max)
    

    
    
    
    


root = TreeNode(50)

root.left=TreeNode(20)
root.left.left=TreeNode(10)
root.left.right=TreeNode(10)
root.left.right.left=TreeNode(20)

root.right=TreeNode(30)
root.right.right=TreeNode(10)
root.right.left=TreeNode(20)



inOrder(root)
print()
print(largetSumTree(root))



    