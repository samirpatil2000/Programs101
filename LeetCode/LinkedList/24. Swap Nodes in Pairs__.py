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
        while ptr and ptr.next:
            print(ptr.val,end=" ")
            ptr=ptr.next
        print(ptr.val,end=" ")  
        print()
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        root.next = head
        
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            prev.next, a.next, b.next = b, b.next, a
            self.printLL(head=root.next)
            prev = a
            print(a.val)
        return root.next
    
    
sol=Solution()
data = [1,2,3,4,5,6]
head = sol.makeLL(data)

sol.printLL(sol.swapPairs(head))