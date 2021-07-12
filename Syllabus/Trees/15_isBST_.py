
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


def makeList(root):
    if(root==None):
        return []
    list=[root.data]
    if(root.right):
        r_list_=makeList(root.right)
        list=list+r_list_
    if(root.left):
        l_list_=makeList(root.left)
        list=list+l_list_
    return list



def is_binary_tree_1(root):
    """ O(n^3) For True Case (Worst Case)"""
    if(root==None):
        return
    if(root.right):
        if(is_binary_tree_1(root.right)):
            r_list_=makeList(root.right)
            for i in r_list_:
                if(i < root.data):
                    return False
        else:
            return False
    if(root.left):
        if(is_binary_tree_1(root.left)):
            l_list_=makeList(root.left)
            for i in l_list_:
                if(i > root.data):
                    return False
        else:
            return False
    return True

def is_Binary_Tree_2(root):
    """ O(n^2) For True Case (Worst Case)"""
    if(root==None):
        return
    list=[root.data]
    if(root.right):
        r_list,is_tree=is_Binary_Tree_2(root.right)
        if(is_tree):
            list+=r_list
            for i in r_list:
                if(i < root.data):
                    return list,False
        else:
            return list,False
    if(root.left):
        l_list,is_tree=is_Binary_Tree_2(root.left)
        if(is_tree):
            list+=l_list
            for i in l_list:
                if(i > root.data):
                    return list,False
        else:
            return list,False
    
    return list,True
    
    
root = newNode(50)
root.left=newNode(25)
root.left.left=newNode(12)
root.left.right=newNode(37)
root.left.right.left=newNode(30)
root.left.right.right=newNode(40)
root.right=newNode(75)
root.right.right=newNode(87)
root.right.left=newNode(62)
root.right.left.right=newNode(70)
root.right.left.left=newNode(60)


print("Main Tree")
display(root)
# print(makeList(root.right))
print(is_binary_tree_1(root))
print(is_Binary_Tree_2(root))