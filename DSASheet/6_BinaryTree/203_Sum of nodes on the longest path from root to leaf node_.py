# https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1
# https://practice.geeksforgeeks.org/problems/sum-tree/1




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
    

def sumOfLongRootToLeafPath(root):
    if root==None:
        return -1,0
    left_height,left_sum=sumOfLongRootToLeafPath(root.left)
    right_height,right_sum=sumOfLongRootToLeafPath(root.right)
    if left_height>right_height:
        return left_height+1,left_sum+root.data
    return right_height+1,right_sum+root.data
    
    
    
    


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
print(sumOfLongRootToLeafPath(root))



    