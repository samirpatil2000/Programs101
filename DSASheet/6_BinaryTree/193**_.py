
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


# root = newNode(50)
# root.left=newNode(25)
# root.right=newNode(75)
# root.right.right=newNode(87)
# root.right.left=newNode(62)
# root.right.left.right=newNode(70)
# root.left.right=newNode(37)
# root.left.right.left=newNode(36)
# root.left.left=newNode(12)

# root=newNode(10)
# root.left=newNode(20)
# root.left.left=newNode(40)
# root.left.right=newNode(50)
# root.right=newNode(30)
# display(root)
s="4(2(3)(1))(6(5))"


def preOrderTraversal(root):
    if root==None:
        return
    print(root.data,end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    

def findIndex(string,start,end):
    st=[]
    for i in range(start,end+1):
        if string[i]=='(':
            st.append(string[i])
        elif string[i]==')':
            if st[len(st)-1]=='(':
                st.pop()
                if len(st)==0:
                    return i
    
        
    
def stringToTree(string,start,end):
    if start>end:
        return None
    root=newNode(ord(string[start]) - ord('0'))
    print(root.data)
    index=-1
    if string[start+1]=='(':
        index=findIndex(string,start+1,end)
    if(index !=-1):
        root.left=stringToTree(string,start+2,index-1)
        root.right=stringToTree(string,index+2,end-1)
    
    return root
    
print(s)

x=stringToTree(s,0,len(s)-1)
preOrderTraversal(x)
print()





