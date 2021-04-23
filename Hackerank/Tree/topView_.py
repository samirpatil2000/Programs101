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

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def dsfRoot(root):
    dict_={}
    queue=[[root,0]]
    while(len(queue)>0):
        for _ in range(len(queue)):
            temp=queue.pop(0)
            curr,col=temp[0],temp[1]
            if not col in dict_:
                dict_[col]=[]
            dict_[col].append(curr.info)
            if curr.left:
                # print("X",curr.left.info)
                queue.append([curr.left,col-1])
            if curr.right:
                queue.append([curr.right,col+1])
    return dict_    
    
    

def topView(root):
    dict_=dsfRoot(root)
    # print(dict_)
    for key in sorted(dict_):
        print(dict_[key][0],end=" ")
    # print()
        
    #Write your code here
    


tree = BinarySearchTree()
# t = int(input())

arr = [12 ,25, 36 ,37 ,50 ,62, 70 ,75 ,87]

for i in range(len(arr)):
    tree.create(arr[i])

topView(tree.root)

    
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.info,end=" ")
    inorder(root.right)    
        
print()
inorder(tree.root)
# print()
# topView(tree.root)
print()
