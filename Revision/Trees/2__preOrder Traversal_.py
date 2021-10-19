from easyBT.binarytree import BinaryTree

class Solution:
    def preOrderIterative(self,root):
        st=[]
        curr=root
        result=[]
        while st or curr:
            if curr:
                result.append(curr.val)
                st.append(curr)
                curr=curr.left
            else:
                curr=st.pop()
                curr=curr.right
        return result



bt=BinaryTree()

nums=[5,3,6,2,4,'*','*',1,0]

root=bt.DesializeTree(nums)

print(bt.PreOrderTraversal(root))

sol=Solution()
print(sol.preOrderIterative(root))

"root - L - R"