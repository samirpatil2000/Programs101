
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sortedArrayToBST(nums):
    if len(nums)==1:
        return TreeNode(nums[0])
    mid=len(nums)//2
    root=TreeNode(nums[mid])
    root.left=TreeNode(nums[0])
    r_=root
    l_=root.left
    
    i=1
    while(i<mid):
        l_.right=TreeNode(nums[i])
        l_=l_.right
        i+=1
    
    i+=1
    while(i<len(nums)):
        r_.right=TreeNode(nums[i])
        r_=r_.right
        i+=1
        
    return root


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
    

# if len(nums)%2==0:
#     root.left=TreeNode(nums[1])
#     root.left.left=TreeNode(nums[0])
# else:
    
    
# nums =[0,1,2,3,4,5]
nums=[-10,-3,0,5,9]
print(len(nums)//2)
root=sortedArrayToBST(nums)
inOrder(root)
print()
print(h(root.left)-h(root.right))
    
    