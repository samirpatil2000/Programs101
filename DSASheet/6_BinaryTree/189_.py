
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
    

def bottomViewUsingBSF(root,dict_):
    queue=[[root,0]]
    while(len(queue)>0):
        for _ in range(len(queue)):
            temp=queue.pop()
            curr,col=temp[0],temp[1]
            if not col in dict_:
                dict_[col]=[]
            dict_[col].append(curr.data)
            if curr.left:
                queue.append([curr.left,col-1])
            if curr.right:
                queue.append([curr.right,col+1])
                
                
    for key in sorted(dict_):
        print(dict_[key][len(dict_[key])-1],end=" ")
    print()
    
    
            
            
            
            
    

    
    



root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(36)
root.left.left=newNode(12)
display(root)

dict_=dict()
bottomViewUsingBSF(root,dict_)
