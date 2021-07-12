class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def display(head):
    left_node=0.0
    right_node=0.0
    if not head:
        return
    if(head.left):
        left_node=head.left.info
    if(head.right):
        right_node=head.right.info
    print(left_node,"<-",head.info,"->",right_node)
    display(head.right)
    display(head.left)

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


tree = BinarySearchTree()


#inorder
arr = [12 ,25, 36 ,37 ,50 ,62, 70 ,75 ,87]

for i in range(len(arr)):
    tree.create(arr[i])
    
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.info,end=" ")
    inorder(root.right)    
        
display(tree.root)
inorder(tree.root)
print()

