# https://leetcode.com/problems/maximum-binary-tree/



# Definition for a binary tree node.
class newNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructMaximumBinaryTree(self, nums):
        
        def fun(nums,left,right):
            if left>right:
                return None
            index_=nums.index(max(nums[left:right+1]))
            root=newNode(nums[index_])
            root.left=fun(nums,left,index_-1)
            root.right=fun(nums,index_+1,right)
            return root
        return fun(nums,0,len(nums)-1)        



def levelOrderTravarsal(root):
    qu=[]
    qu.append(root)
    list_=[root.val]
    while(len(qu)>0):
        for _ in range(len(qu)):
            temp=qu.pop(0)
            
            
            if(temp.left):
                list_.append(temp.left.val)
                qu.append(temp.left)
            else:
                list_.append(None)
            if(temp.right):
                list_.append(temp.right.val)
                qu.append(temp.right)
            else:
                list_.append(None)
        # print('\n')
    return list_
    
      

def inOrder(root):
    if(root==None):
        return
    inOrder(root.left)
    print(root.val, end=" ")
    inOrder(root.right)


sol=Solution()
nums=[3,2,1,6,0,5]
print(levelOrderTravarsal(sol.constructMaximumBinaryTree(nums)))
print()