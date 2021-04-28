# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
# https://practice.geeksforgeeks.org/problems/sum-tree/1




class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class ListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None


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
    
    
def boudary(root):
    queue=[root]
    st=[]
    boudary_arr=[]
    while(len(queue)>0):
        x=len(queue)
        for i in range(x):
            temp=queue.pop(0)
            if i==0:
                boudary_arr.append(temp.data)
            elif i==x-1 and i!=0:
                st.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
    st.reverse()
    boudary_arr+=st    
    return boudary_arr




    


root = TreeNode(20)

root.left=TreeNode(8)
root.left.left=TreeNode(4)
root.left.right=TreeNode(12)
root.left.right.left=TreeNode(10)
root.left.right.right=TreeNode(14)

root.right=TreeNode(22)
root.right.right=TreeNode(25)
# root.right.left=TreeNode(20)
# 20 8 4 10 14 25 22


inOrder(root)
print()

print(boudary(root))



