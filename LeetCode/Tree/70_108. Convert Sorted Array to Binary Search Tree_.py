
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sortedArrayToBST(nums):
    #se recurseion walking 
    pass


def h(root):
    if root==None:
        return -1
    return max(h(root.left),h(root.right))+1     
            
def inOrder(root):
    if(root==None):
        return
    print(root.val, end=" ")
    inOrder(root.left)
    inOrder(root.right)
    
    
# nums =[0,1,2,3,4,5]
nums=[-10,-3,0,5,9]
print(len(nums)//2)
root=sortedArrayToBST(nums)
inOrder(root)
print()
print(h(root.left)-h(root.right))
    
    