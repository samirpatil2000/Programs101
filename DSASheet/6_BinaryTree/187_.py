
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


def rightView(root):
    queue=[root]
    right_view=[]
    while(len(queue)):
        
        x=len(queue)
        for i in range(x):
            temp=queue.pop(0)
            if i==x-1:
                right_view.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    return right_view
        
        

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


root = newNode(5)
root.left = newNode(3)
root.right = newNode(6)
root.right.left=newNode(7)
root.left.left = newNode(2)
root.left.left.left = newNode(1)
root.left.right = newNode(4)
root.left.left.left.left = newNode(0)
display(root)

print(rightView(root))