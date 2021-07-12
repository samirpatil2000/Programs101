
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

def height(root):
    if(root==None):
        return -1
    return max(height(root.left),height(root.right))+1

def diameterOfTRee(root):
    """O(n^2)"""
    if(root==None):
        return 0
    ld=diameterOfTRee(root.left)
    rd=diameterOfTRee(root.right)
    f=height(root.left)+height(root.right)+2
    return max(f,max(ld,rd));

def diameterOfTreeWithHeight(root):
    """O(n^1)"""
    if(root==None):
        return 0,-1
    ld,left_height=diameterOfTreeWithHeight(root.left)
    rd,right_height=diameterOfTreeWithHeight(root.right)
    f=left_height+right_height+2
    return max(f,max(ld,rd)),max(left_height,right_height)+1;
   
    



        

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
print("Main Tree")
display(root)
print("The height = ",height(root))
print("The diameter = ",diameterOfTRee(root))

print("The height and the diameter",diameterOfTreeWithHeight(root))