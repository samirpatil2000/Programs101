
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

def kLevelDown(root,k,block_node):
    if(root== None or k<0 or root==block_node):
        return
    if(k==0):
        print(root.data)
        return
    else:
        kLevelDown(root.left,k-1,block_node)
        kLevelDown(root.right,k-1,block_node)
        return
    
    
def nodeToRoot_2(root,val):
    path=[]
    if(root == None):
        return False,[]
    if(root.data == val):
        path.append(root)
        return True,path
    if(root.left):
        findLeftChild,left_path=nodeToRoot_2(root.left,val)
        if(findLeftChild):
            path.append(root)
            path=path+left_path
            return True,path
    if(root.right):
        findRightChild,right_path=nodeToRoot_2(root.right,val)
        if(findRightChild):
            path.append(root)
            path=path+right_path
            return True,path
    return False,[]


def print_k_level_far(root,val,k):
    paths=nodeToRoot_2(root,val)[1]
    paths.reverse()
    print("The Paths are")
    for i in range(len(paths)):
        if(i==0):
            block_node=None
            kLevelDown(paths[i],k-i,block_node)
        else:
            kLevelDown(paths[i],k-i,paths[i-1])
    return
        
            
        

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

display(root)
paths=nodeToRoot_2(root,70)[1]
# nodes=[]
# for i in paths:
#     nodes.append(i.data)
# print(nodes)

print_k_level_far(root,50,2)