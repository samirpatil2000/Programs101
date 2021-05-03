
# https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/



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
    
    
def makeDict_(root,dict_):
    if root==None:
        return
    if root.left:
        dict_[root.left.data]=root.data
        makeDict_(root.left,dict_)
    if root.right:
        dict_[root.right.data]=root.data
        makeDict_(root.right,dict_)
    
def getKthAccenstor(k,node,dict_):
    acc=None
    X=node
    while(k>0):
        acc=dict_[X]
        X=acc
        
        k-=1
        if acc==-1:
            break
    print(acc)
    
    
        
       
    
root = newNode(50)

root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)

root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)




dict_={}
dict_[root.data]=-1
makeDict_(root,dict_)
print(dict_)

getKthAccenstor(4,70,dict_)
