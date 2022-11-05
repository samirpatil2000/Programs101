from easyBT.binarytree import BinaryTree
bt = BinaryTree()
nums = [1,2,3,4,5,6,7]
root = bt.DesializeTree(nums)

class solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

