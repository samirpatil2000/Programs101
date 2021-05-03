# https://leetcode.com/problems/cousins-in-binary-tree/


import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inOrder(root):
    if(root==None):
        return
    print(root.val, end=" ")
    inOrder(root.left)
    inOrder(root.right)


# [1,2,3,null,4,null,5],

root=TreeNode(1)
root.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right=TreeNode(3)

root.right.right=TreeNode(5)




class Solution:
    def fun(self,arr,x,y):
        x_parent,y_parent=None,None
        count=0
        for i in range(len(arr)):
            if x==arr[i][0].val:
                count+=1
                x_parent=arr[i][1]
                print(x_parent.val)
            elif y==arr[i][0].val:
                count+=1
                y_parent=arr[i][1]
                print(y_parent.val)
            if count==2:
                print(x_parent.val,y_parent.val)
                if x_parent!=y_parent:
                    return True
                else:
                    return False
        return False
                
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue=[[root,None]]
        while(len(queue)>0):
            l=len(queue)
            if l>1:
                print([i[0].val for i in queue])
                if self.fun(queue,x,y):
                    return True
            
            for _ in range(l):
                temp=queue.pop(0)[0]
                if temp.left:
                    queue.append([temp.left,temp])
                if temp.right:
                    queue.append([temp.right,temp])
        return False
    
    
sol=Solution()
x = 5
y = 4
print(sol.isCousins(root,x,y))


