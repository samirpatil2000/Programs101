# Convert Binary tree into Sum tree
# https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1



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


root = newNode(10)

root.left=newNode(-2)
root.left.left=newNode(8)
root.left.right=newNode(-4)

root.right=newNode(6)
root.right.right=newNode(5)
root.right.left=newNode(7)






def convertBinaryTreeToSumTree(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        prev_data=root.data
        root.data=0
        return prev_data
    
    pre_data=root.data
    root.data=0
    if root.left:
        left_root=convertBinaryTreeToSumTree(root.left)
        root.data+=left_root
    if root.right:
        right_root=convertBinaryTreeToSumTree(root.right)
        root.data+=right_root
    pre_data+=root.data
    return pre_data
    

    

inOrder(root)
print()
convertBinaryTreeToSumTree(root)
inOrder(root)
print()





