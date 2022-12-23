from typing import List


class Node:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        
        
class LinkedList:
    
    def __init__(self, head=None):
        self.head = head
        
        
    def create(self, arr: List[int]):
        if not arr: return
        
        root = self.get_last_node()
        if not root:
            self.head = Node(arr[0])
            root = self.head

        for i in range(len(arr) - 1):
            root.next = Node(arr[i + 1])
            root = root.next
            
            
    def get_last_node(self, head=None):
        root = head or self.head
        while root and root.next:
            root = root.next
        return root

        
    def print(self, head=None):
        temp = head or self.head
        while temp and temp.next:
            print(str(temp.val) + " -> ",end="")
            temp = temp.next
        print(str(temp.val))
        
        
    def append(self, val, head=None):
        temp = head or self.head
        new_node = Node(val)
        if temp == None:
            temp = new_node
        else:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
            
    def get_middle_node(self, head=None):
        temp = head or self.head
        slow = temp
        fast = temp
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    
    
arr = [0, 2, 4, 6, 3, 9, 1]
ll = LinkedList()
ll.create(arr)
ll.print()