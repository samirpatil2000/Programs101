
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)



def returnNode(root,val):
    if root==None:
        return None
    if root.data==val:
        return root
    val_node=returnNode(root.left,val)
    if val_node==None:
        val_node=returnNode(root.right,val)
    return val_node

nodes=[]
def returnNodeWithRep(root,val):
    if root==None:
        return None
    if root.data==val:
        nodes.append(root)
    returnNodeWithRep(root.left,val)
    returnNodeWithRep(root.right,val)


def isEqualFunction(rootA,rootB):
    if rootA==None and rootB==None:
        return True
    if rootA and rootB and rootA.val==rootB.val:
        if isEqualFunction(rootA.left,rootB.val) and isEqualFunction(rootA.right,rootB.left):
            return True
    return False
    
    
    
    



root = newNode(50)
root.left=newNode(25)
root.right=newNode(75)
root.right.right=newNode(57)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.left.right=newNode(37)
root.left.right.left=newNode(62)
root.left.left=newNode(12)
# display(root)
inOrder(root)
print()

try:
    print(returnNode(root,72).data)
except:
    print("No node found .!")


returnNodeWithRep(root,62)
print(nodes,[node.data for node in nodes])