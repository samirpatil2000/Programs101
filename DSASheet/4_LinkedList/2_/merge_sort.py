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
    
    
    def get_middle(self, end_val, left_node=None):
        temp = left_node or self.head
        slow = fast = temp
        while fast and fast.val != end_val and fast.next and fast.next.val != end_val:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def merge_two_sorted_ll(self, node_a: "Node", node_b: "Node"):
        result = None
        if node_a == None:
            return node_b
        if node_b == None:
            return node_b
        
        if node_a.val <= node_b.val:
            result = node_a
            result.next = self.merge_two_sorted_ll(node_a.next, node_b)
        else:
            result = node_b
            result.next = self.merge_two_sorted_ll(node_a, node_b.next)
        return result
    
    
class Solution:
    
    def merge_ll(self, node_a: "Node", node_b: "Node"):
        result = None
        if node_a == None:
            return node_b
        if node_b == None:
            return node_a
        
        if node_a.val <= node_b.val:
            result = node_a
            result.next = self.merge_ll(node_a.next, node_b)
        else:
            result = node_b
            result.next = self.merge_ll(node_a, node_b.next)
        return result
    
    def sort(self, head, ll: "LinkedList"):
        if not head or not head.next:
            return head
        
        middle_node = ll.get_middle_node(head)
        next_middle_node = middle_node.next
        middle_node.next = None
        
        left_node = self.sort(head, ll)
        right_node = self.sort(next_middle_node, ll)
        return self.merge_ll(left_node, right_node)
    
    def sort_ll(self, ll: "LinkedList"):
        return self.sort(ll.head, ll)

    
arr = [0, 2, 4, 6, 3, 9, 1]
ll = LinkedList()
ll.create(arr)
ll.print()
ll.print (Solution().sort(ll.head, ll))
