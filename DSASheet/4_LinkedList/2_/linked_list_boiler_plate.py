from typing import List


class Node:
    def __init__(self, data=-1):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        
    def create(self, arr: List[int]):
        if not arr:
            return
        
        root = self.get_last_node()
        if not root:
            self.head = Node(arr[0])
            root = self.head

        for i in range(len(arr)):
            root.next = Node(arr[i])
            root = root.next
            
            
    def get_last_node(self, head=None):
        root = head or self.head
        while root and root.next:
            root = root.next
        return root

        
    def print(self, head=None):
        temp = head or self.head
        while temp and temp.next:
            print(str(temp.data) + " -> ",end="")
            temp = temp.next
        print(str(temp.data))
        
        
    def append(self, data, head=None):
        temp = head or self.head
        new_node = Node(data)
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
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow