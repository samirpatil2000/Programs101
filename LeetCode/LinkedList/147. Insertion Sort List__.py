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
        
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        dummyHead=ListNode(val=-5001)
        dummyHead.next=head
        curr=head
        while curr and curr.next:
            if curr.val<=curr.next.val:
                curr=curr.next
            else:
                toInsert=curr.next
                preInsert=dummyHead
                while preInsert.next and preInsert.next.val<toInsert.val:
                    preInsert=preInsert.next
                curr.next=toInsert.next
                toInsert.next=preInsert.next
                preInsert.next=toInsert
        return dummyHead.next
        
sol=Solution()
arr =  [2,-3,4]
head=sol.makeLL(arr)
sol.printLL(head)

sol.printLL(sol.insertionSortList(head))