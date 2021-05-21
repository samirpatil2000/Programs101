

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        



class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp.next):
            print(str(temp.val) + "->",end="")
            temp = temp.next
        print(str(temp.val))
        print("\n");

    def addNodeToLast(self, data):
        new_node = ListNode(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
    
                
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getLastNode(self,head):
        temp=head
        while(temp.next != None):
            temp=temp.next
        return temp
    def getMid(self,left_node,right_node):
        slow=left_node
        fast=left_node
        while fast and fast.next!=right_node and fast.next.next!=right_node:
            print(slow.val,fast.val)
            fast=fast.next.next
            slow=slow.next
            
        return slow
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def dfs(left_node,right_node):
            
            mid_node=self.getMid(left_node,right_node)
            root=TreeNode(mid_node.val)
            root.left=dfs(left_node,mid_node)
            root.right=dfs(mid_node.next,right_node)
            
            return root
        return dfs(head,self.getLastNode(head))

def inOrder(root):
    if root==None:
        return
    inOrder(root.left)
    print(root.val,end=" ")
    inOrder(root.right)
    


linkedListA = LinkedList()
linkedListA.addNodeToLast(3)
linkedListA.addNodeToLast(4)
linkedListA.addNodeToLast(2)
linkedListA.addNodeToLast(7)
linkedListA.addNodeToLast(10)
linkedListA.addNodeToLast(9)
linkedListA.addNodeToLast(11)

sol=Solution()

x=sol.sortedListToBST(linkedListA.head)
inOrder(x)
print()