
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


def leftView(root):
    queue=[root]
    left_view=[]
    while(len(queue)):
        left_view.append(queue[0].data)
        for _ in range(len(queue)):
            temp=queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    return left_view
        
    
            
            
    
        
            
    
    
    


    
    
        

        

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


# root = newNode(5)
# root.left = newNode(3)
# root.right = newNode(6)
# root.right.left=newNode(7)
# root.left.left = newNode(2)
# root.left.left.left = newNode(1)
# root.left.right = newNode(4)
display(root)

print(leftView(root))