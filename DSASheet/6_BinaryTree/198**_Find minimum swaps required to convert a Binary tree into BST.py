

# https://www.geeksforgeeks.org/minimum-swap-required-convert-binary-tree-binary-search-tree/

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



def makeATree(arr,i):
    if i>=len(arr):
        return None
    root=TreeNode(arr[i])
    root.left=makeATree(arr,2*i+1)
    root.right=makeATree(arr,2*i+2)
    return root

def makeInOrderWithTree(arr):
    
    root=makeATree(arr,0)
    inOrder(root)
    

def makeInOrderWithoutTree(arr,i,list_):
    if i>=len(arr):
        return
    makeInOrderWithoutTree(arr,2*i+1,list_)
    list_.append(arr[i])
    makeInOrderWithoutTree(arr,2*i+2,list_)
    
    
    
    

arr = [1,2,3]
print()

# makeInOrderWithTree(arr)
inOrderList=[]
makeInOrderWithoutTree(arr,0,inOrderList)
# print(inOrderList)




# USING SELECTION SORT ALGO
def smallestElement(arr,left):
    min_=left
    for i in range(left,len(arr)):
        if arr[min_]>arr[i]:
            min_=i
    return min_

def minSwapRequieredToSwap(inOrderList_):
    count=0
    for i in range(len(inOrderList_)):
        min_=smallestElement(inOrderList_,i)
        if inOrderList_[min_]<inOrderList_[i]:
            inOrderList_[i],inOrderList_[min_]=inOrderList_[min_],inOrderList_[i]
            count+=1
    return count
print(minSwapRequieredToSwap(inOrderList))











    