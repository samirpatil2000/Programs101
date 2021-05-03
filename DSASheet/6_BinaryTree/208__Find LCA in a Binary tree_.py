# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1



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
    

def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.data,end=" ")
    inOrder(root.right)

path_n1=""
path_n2=""
def lowestCommanA(root,n1,n2,psf_n1,psf_n2):
    global path_n1,path_n2
    if root==None:return
    
    if root.data==n1:
        # psf_n1+=str(root.data)
        path_n1=psf_n1
        return
    if root.data==n2:
        path_n2=psf_n2
        return
    
    if root.left:
        lowestCommanA(root.left,n1,n2,psf_n1+","+str(root.left.data),psf_n2+","+str(root.left.data))
    
    if root.right:
        lowestCommanA(root.right,n1,n2,psf_n1+","+str(root.right.data),psf_n2+","+str(root.right.data))
        
    return


root = newNode(50)

root.left=newNode(25)


root.right=newNode(75)
root.right.left=newNode(62)
root.right.right=newNode(85)

root.right.left.right=newNode(70)

root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.left=newNode(12)



inOrder(root)
print()


lowestCommanA(root,70,85,str(root.data),str(root.data))
path_n1=[int(i) for i in path_n1.split(",")]
path_n2=[int(i) for i in path_n2.split(",")]
print(path_n1,path_n2)
def lowestCom():
    
    i,j=0,0
    while path_n1[i]==path_n2[j]:
        i+=1
        j+=1
    return path_n1[i-1],path_n2[j-1]
        
    
    
# print(path_n1,"---",path_n2)
print()
print(lowestCom())
    