# https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/

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


    
def printKSumPath(root,path,k):
    if not root:return
    path.append(root.data)
    printKSumPath(root.left,path,k)
    printKSumPath(root.right,path,k)
    
    f=0
    path_=""
    i=len(path)-1
    while(i>=0):
        f+=path[i]
        path_+=str(path[i])+","
        if f==k:
            print(path_)
            printKSumPath.counter+=1
            # break
        i-=1
    path.pop()
    
    
    
    
    
    
    
    


root = newNode(1) 
root.left = newNode(3) 
root.left.left = newNode(2) 
root.left.right = newNode(1) 
root.left.right.left = newNode(1) 
root.right = newNode(-1) 
root.right.left = newNode(4) 
root.right.left.left = newNode(1) 
root.right.left.right = newNode(2) 
root.right.right = newNode(5) 
root.right.right.right = newNode(2)



inOrder(root)
print()

k = 5
path=[]
printKSumPath.counter=0
printKSumPath(root, path,k)
print(printKSumPath.counter)