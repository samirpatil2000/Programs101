
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
    if(root==None):
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)


def verticalOrderTraversal(root,dict_,row,col):
    if root==None:
        return
    # print(root.data,dict_)
    if not row in dict_:
        dict_[row]=dict()
    dict_[row].update({col:root.data})
    
    verticalOrderTraversal(root.left,dict_,row+1,col-1)
    verticalOrderTraversal(root.right,dict_,row+1,col+1)
    
    
def verticalOrderUsingBSF(root,dict__):
    queue=[[root,0]]
    while(len(queue)>0):
        for _ in range(len(queue)):
            temp=queue.pop()
            col=temp[1]
            curr=temp[0]
            if not col in dict__:
                dict__[col]=list()
            dict__[col].append(curr.data)
            if curr.left:
                queue.append([curr.left,col-1])
            if curr.right:
                queue.append([curr.right,col+1])
    print(dict__)

            
            
            
            
    

    
    



root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(36)
root.left.left=newNode(12)
display(root)
# inOrder(root)
# print()
dict_=dict()
dict_[0]=dict()
verticalOrderTraversal(root,dict_,0,0)
print(dict_)

dict__=dict()
dict__[0]=[]
verticalOrderUsingBSF(root,dict__)