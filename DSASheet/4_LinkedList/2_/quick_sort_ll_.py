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
    

class Solution:
    
    def paritionLast(self, start, end):
        if (start == end or start == None or end == None):
            return start
 
        pivot_prev = start
        curr = start
        pivot = end.val
 
        '''iterate till one before the end,
        no need to iterate till the end because end is pivot'''
 
        while (start != end):
            if (start.val < pivot):
 
                # keep tracks of last modified item
                pivot_prev = curr
                temp = curr.val
                curr.val = start.val
                start.val = temp
                curr = curr.next
            start = start.next
 
        '''swap the position of curr i.e.
        next suitable index and pivot'''
 
        temp = curr.val
        curr.val = pivot
        end.val = temp
 
        ''' return one previous to current because
        current is now pointing to pivot '''
        return pivot_prev
    
    def partiation(self, start: "Node", end: "Node"):
        head = curr = prev = Node()
        curr.next = start
        curr = curr.next
        end_ptr = end
        while curr and end and curr != end:
            if curr.val > end.val:
                curr_next = curr.next
                prev.next = curr.next
                curr.next = None
                end_ptr.next = curr
                curr = curr_next
                end_ptr = end_ptr.next
            else:
                prev = prev.next
                curr = curr.next
        return head.next, end
    
    
    def quick_sort(self, start: "Node", end: "Node", ll: "LinkedList"):
        pivot_location =  self.partiation(start, end)
        pivot_location.next = None
        next_pivot_location = pivot_location.next
        self.quick_sort(start, pivot_location, ll)
        self.quick_sort(next_pivot_location, ll)
        return left
    
arr = [0, 2, 4, 6, 3, 9, 1]
arr = [2, 6, 0, 3]
ll = LinkedList()
ll.create(arr)
ll.print()

sol = Solution()
# head, location = sol.partiation(ll.head, end=ll.get_last_node())
location = sol.paritionLast(ll.head, end=ll.get_last_node())
# ll.print(head)
ll.print(location)
