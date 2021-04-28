# https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1


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
    
# isLeafAtSameLevel.dict_=0
def isLeafAtSameLevel(root,level):
    if root==None:
        return True
    if root and root.left==None and root.right==None:
        if isLeafAtSameLevel.const==0:
            isLeafAtSameLevel.const=level
            return True
        elif isLeafAtSameLevel.const==level:
            return True
        return False   
    if isLeafAtSameLevel(root.left,level+1) and isLeafAtSameLevel(root.right,level+1):
        return True
    return False
    
    
    


root = TreeNode(50)

root.left=TreeNode(20)

root.left.left=TreeNode(10)
root.left.right=TreeNode(10)

root.right=TreeNode(30)
root.right.right=TreeNode(10)
# root.right.left=TreeNode(20)

isLeafAtSameLevel.const=0

inOrder(root)
print()

print(isLeafAtSameLevel(root,0))




    