# Convert Binary tree into Doubly Linked List
# Convert Binary tree into Sum tree
# https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1



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
    
    
def makeDoublyLinkedList(tree_root):
    if tree_root==None:
        return
    makeDoublyLinkedList(tree_root.left)
    
    print(tree_root.data,makeDoublyLinkedList.prev_node.data,"before")
    makeDoublyLinkedList.prev_node.right=tree_root
    makeDoublyLinkedList.prev_node.right.left=makeDoublyLinkedList.prev_node
    makeDoublyLinkedList.prev_node=makeDoublyLinkedList.prev_node.right
    print(tree_root.data,makeDoublyLinkedList.prev_node.data,"after")
    
    makeDoublyLinkedList(tree_root.right)
    
    
# def makeDoublyLinkedListWithIteration(tree_root,list_head):
    
    
    
    
    
    
def printDoublyLL(list_head):
    temp=list_head
    while temp and temp.right:
        print(temp.data,end=" ")
        temp=temp.right
    print(temp.data,end=" ")
    print()
    
    
    
    


root = TreeNode(10)

root.left=TreeNode(2)
root.left.left=TreeNode(8)
root.left.right=TreeNode(4)

root.right=TreeNode(6)
root.right.right=TreeNode(5)
root.right.left=TreeNode(7)

list_node=TreeNode(0)


inOrder(root)
print()
printDoublyLL(list_node)
print()
makeDoublyLinkedList.prev_node=list_node
makeDoublyLinkedList(root)
print("The Doubly LL")
printDoublyLL(list_node.right)



print()





