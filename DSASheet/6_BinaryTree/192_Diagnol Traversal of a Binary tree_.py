
from collections import deque
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
    
    
def usingDFS(root,d,dict_):
    if root==None:
        return
    if not d in dict_:
        dict_[d]=[]
    dict_[d].append(root.data)
    usingDFS(root.left,d+1,dict_)
    usingDFS(root.right,d,dict_)

def usingBSF(root):
    dict_={}
    queue=[[root,0]]
    while(len(queue)>0):
        for _ in range(len(queue)):
            temp=queue.pop(0)
            if not temp[1] in dict_:
                dict_[temp[1]]=[]
            dict_[temp[1]].append(temp[0].data)
            if temp[0].left:
                queue.append([temp[0].left,temp[1]+1])
            if temp[0].right:
                queue.append([temp[0].right,temp[1]])
    return dict_
    
    
def usingIterativeApproach(root):
    queue=[]
    out=[]
    node=root
    while node:
        out.append(node.data)
        if node.left:
           queue.append(node.left)
        if node.right:
            node=node.right
        else:
            if len(queue)>0:
                node=queue.pop(0)
            else:
                node=None
    return out
                
                
    

    
            
    

    
    
            
            
            
            
    

    
    



root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(36)
root.left.left=newNode(12)

# root=newNode(10)
# root.left=newNode(20)
# root.left.left=newNode(40)
# root.left.right=newNode(50)
# root.right=newNode(30)
display(root)


dict_={}
usingDFS(root,0,dict_)
print(dict_)

print(usingIterativeApproach(root))
print(usingBSF(root))