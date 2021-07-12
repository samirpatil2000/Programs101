
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def display(head):
    left_node=0.0
    right_node=0.0
    if head==None:
        return
    if(head.left):
        left_node=head.left.data
    if(head.right):
        right_node=head.right.data
    print(left_node,"<-",head.data,"->",right_node)
    display(head.right)
    display(head.left)
    
# global tilt_
tilt_=0
def tilt(root):
    if(root==None):
        return 0,0
    if(root.left==None and root.right==None):
        return root.data,0
    l_sum=r_sum=0
    l_tilt=r_tilt=0
    if(root.left):
        l_sum,l_tilt=tilt(root.left)
    if(root.right):
        r_sum,r_tilt=tilt(root.right)
    total_sum=r_sum+l_sum+root.data
    
    return total_sum,abs(r_sum-l_sum)+l_tilt+r_tilt
    
    
root = newNode(50)
root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)

# root = newNode(10)
# root.left=newNode(10)
# root.left.left=newNode(10)
# root.left.right=newNode(10)
# root.left.right.left=newNode(10)
# root.left.right.right=newNode(10)
# root.right=newNode(10)
# root.right.right=newNode(10)
# root.right.left=newNode(10)
# root.right.left.right=newNode(10)
# root.right.left.left=newNode(10)
print("Main Tree")
display(root)
print("The tilt = ",tilt(root))