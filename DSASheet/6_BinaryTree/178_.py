
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


def levelOrderTravarsal(root):
    qu=[]
    qu.append(root)
    list_=[]
    while(len(qu)>0):
        for _ in range(len(qu)):
            temp=qu.pop(0)
            if(temp.left):
                qu.append(temp.left)
            if(temp.right):
                qu.append(temp.right)
            print(temp.data,end=" ")
        print('\n')
    
        
            
    
        

        

root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
root.left.left=newNode(12)
display(root)
levelOrderTravarsal(root)