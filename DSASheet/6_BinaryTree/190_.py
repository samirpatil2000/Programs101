
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
    

def zigzagtraversal(root):
    queue=[root]
    count=0
    while(len(queue)>0):
        for _ in range(len(queue)):
            curr=queue.pop(0)
            print(curr.data,end=" ")
            if count==0 or count%2==0:
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            else:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
        print("\n")
        count+=1
        
                
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

zigzagtraversal(root)
