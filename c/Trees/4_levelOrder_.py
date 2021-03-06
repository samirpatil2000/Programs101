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
    
def levelOrder(root):
    q=deque()
    q.append(root)
    while(len(q)>0):
        count=len(q)
        for _ in range(count):
            node=q.popleft()
            print(node.data,end=" ")
            if(node.left !=None):
                q.append(node.left)
            if(node.right !=None):
                q.append(node.right)
        print("\n")
    return

    
    

root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(37)
root.left.left=newNode(12)
display(root)
levelOrder(root)
