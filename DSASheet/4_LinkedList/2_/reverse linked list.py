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
        return head.next
    
    
    def print_ll(self, head: "Node"):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()
    
    def reverse_ll(self, head: "Node"):
        new_head = None
        while head:
            ptr = head.next
            head.next = new_head
            new_head = head
            head = ptr
        return new_head

arr = [1, 2, 3, 4, 5]

sol = Solution()
head = sol.create_ll(arr)
sol.print_ll(head)
sol.print_ll(sol.reverse_ll(head))
			
		