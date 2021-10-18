from easyBT.binarytree import BinaryTree

class Solution:
    def inOrderIterative(self,root):
        st=[]
        curr=root
        result=[]
        while(len(st)>0 or curr):
            if(curr):
                st.append(curr)
                curr=curr.left
            else:
                curr=st.pop()
                result.append(curr.val)
                curr=curr.right
        return result



bt=BinaryTree()

nums=[5,3,6,2,4,'*','*',1,0]

root=bt.DesializeTree(nums)

print(bt.InOrderTraversal(root))

sol=Solution()
print(sol.inOrderIterative(root))

"L - root - R"