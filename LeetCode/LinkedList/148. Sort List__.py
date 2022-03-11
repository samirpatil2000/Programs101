from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeList(self, head1:ListNode, head2:ListNode):
        root = ListNode()
        while head1 and head2:
            if head1.val >= head2.val:
                root.next = head2
                head2 = head2.next
            else:
                root.next = head1
                head1 = head1.next
            root = root.next
        if head1:
            root.next = head1
        elif head2:
            root.next = head2
        return root.next
    def find_mid(self, start, end):
        sptr = start
        fptr = start
        while fptr and fptr.next and fptr.next.next and end not in (fptr, fptr.next, fptr.next.next):
            sptr = sptr.next
            fptr = fptr.next.next
        return sptr
    def merge(self, start: ListNode, end:ListNode):
        if start != end:
            mid = self.find_mid(start, end)
            self.merge(start, mid)
            temp, mid.next = mid.next, None
            self.merge(temp, end)
            self.mergeList(start, mid.next)
        
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.merge()
    


sol = Solution()
print(sol.sortList())

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halfs
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.merge(left, right)
    
    def getMid(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # Merge the list
    def merge(self, list1, list2):
        newHead = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return newHead.next