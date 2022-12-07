class Node:
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = None
        
class Solution:
    
    def create_ll(self, arr: list):
        head = Node()
        root = head
        for i in arr:
            root.next = Node(i)
            root = root.next
        return head
    
    
    def print_ll(self, head: "Node"):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()
        
    def find_middle(self, head: "Node"):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    


sol = Solution()
arr = [1, 2, 3, 4, 5]
head = sol.create_ll(arr)
sol.print_ll(head.next)
print(sol.find_middle(head))

      
            