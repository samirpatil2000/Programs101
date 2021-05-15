# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        list_=[]        
        def nodeToRootPath(root,target):
            if root==None:return None
            if root.val==target:
                return [root]
            f_l=nodeToRootPath(root.left,target)
            if f_l:    
                return f_l+[root]
            f_r=nodeToRootPath(root.right,target)
            if f_r:
                return f_r+[root]
            return None
        path_list=nodeToRootPath(root,target)
        
        def kLevelDown(root,k,block):
            if root==None or k<0:
                return
            if block==root:
                return
            if k==0:
                list_.append(root.val)
                return
            kLevelDown(root.left,k-1,block)
            kLevelDown(root.right,k-1,block)
            
        for i in range(len(path_list)):
            # 
            block=None
            if i>0:
                block=path_list[i-1]
            # print(path_list[i].val,k-i,block)
            kLevelDown(path_list[i],k-i,block)
        
        print(path_list)
        
            
        return list_

root=TreeNode(3)

root.left=TreeNode(5)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)

root.right=TreeNode(1)
root.right.right=TreeNode(8)
root.right.left=TreeNode(0)



sol=Solution()

target = 5
k = 2
print(sol.distanceK(root,target,k))


# stdout.write(style.SUCCESS('Data imported successfully'))
# print("\033
# [1;32;40m Bright Green")
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')