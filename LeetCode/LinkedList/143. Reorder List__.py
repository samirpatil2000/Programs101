from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def makeLL(self,arr:List[int])->ListNode:
        head=ListNode(arr[0])
        ptr=head
        for i in range(1,len(arr)):
            ptr.next=ListNode(arr[i])
            ptr=ptr.next
        return head
    def printLL(self,head):
        ptr=head
        while ptr:
            print(ptr.val,end=" ")
            ptr=ptr.next
        print()
    def reorderList(self, head):
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp    
        slow.next = None
        
        
        #step 3: merge lists
        head1, head2 = head, prev
        self.printLL(head1)
        self.printLL(head2)
        while head2:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
            

sol=Solution()
data=[1,2,3,4,5,6]
head=sol.makeLL(data)
sol.reorderList(head)
sol.printLL(head)