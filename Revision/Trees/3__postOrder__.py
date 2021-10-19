from easyBT.binarytree import BinaryTree

class Solution:
    def PostOrder(self,root):
        result=[]
        temp=root
        def dfs(root):
            if not root:return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        dfs(temp)
        return result
            
    def postOrderIterative(self,node):
        st=[]
        result=[]
        root=node
        while st or root:
            if root:
                result.append(root.val)
                st.append(root)
                root=root.right
            else:
                root=st.pop()
                
                root=root.left
        return result[::-1]
                



bt=BinaryTree()

nums=[5,3,6,2,4,'*','*',1,0]

root=bt.DesializeTree(nums)
print(bt.PostOrderTraversal(root))

sol=Solution()
print(sol.postOrderIterative(root))
# print(sol.PostOrder(root))
"L - R - root"