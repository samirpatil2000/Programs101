# https://leetcode.com/problems/symmetric-tree/
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







def isSymmetric(root):
    queue=[root]
    
    while(len(queue)>0):
        level_order_list=[]
        for _ in range(len(queue)):
            temp=queue.pop(0)
            
            if temp.left:
                queue.append(temp.left)
                level_order_list.append(temp.left.val)
            else:
                level_order_list.append(200)
                
            if temp.right:
                queue.append(temp.right)
                level_order_list.append(temp.right.val)
            else:
                level_order_list.append(200)
                
        i=0
        j=len(level_order_list)-1
        while(i<j):
            if level_order_list[i]!=level_order_list[j]:
                return False
            i+=1
            j-=1
    return True
