


class newNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        

class Tree_():
    def __init__(self) -> None:
        self.root=None
        
    def addNodeToTree(self,val):
        if(self.root==None):
            self.root=newNode(val)
        else:
            parentNode=None
            root_node=self.root
            while(root_node):
                parentNode=root_node
                # print(root_node.val)
                if(root_node.left==None and root_node.right==None):
                    break
                
                if(root_node.right and val > root_node.val):
                    root_node=root_node.right
                elif(root_node.left):
                    root_node=root_node.left
            if(parentNode.val>val):
                parentNode.left=val
            else:
                parentNode.right=val
                
        


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
    

    




list_=[50,25,75,57,62,70,37,37,12]


root=Tree_()
for i in list_:
    root.addNodeToTree(i)

display(root)
    

