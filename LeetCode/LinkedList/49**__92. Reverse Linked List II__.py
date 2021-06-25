# Definition for singly-linked list.
from typing import List, Pattern


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
    def reverseLL(self,head:ListNode)->ListNode:
        newHead=None
        while head and head.next:
            ptr=head.next 
            head.next=newHead
            newHead=head
            head=ptr
        if head:
            head.next=newHead
        return head
           
        
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # if left==right:
        #     return head
        # left-=1
        # right-=1
        # left_ptr=head
        # right_ptr=head
        # while left>1:
        #     left-=1
        #     left_ptr=left_ptr.next
        # while right>0:
        #     right-=1
        #     right_ptr=right_ptr.next
        # print(right_ptr.val)
            
        # tail=right_ptr.next
        # right_ptr.next=None
        
        # rev=self.reverseLL(left_ptr.next)
        # left_ptr.next=rev
        # while rev and rev.next:
        #     rev=rev.next
        # if rev:
        #     rev.next=tail
        
        # return head
        if not head or left==right:return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        for _ in range(left-1):
            p=p.next
        tail=p.next
        
        for _ in range(right-left):
            temp=p.next
            p.next=tail.next
            tail.next=tail.next.next
            p.next.next=temp
        return dummy.next
            
            
    
        
            
        
sol=Solution()
arr = [3,5]
head=sol.makeLL(arr)
# sol.printLL(head)
left = 1
right = 2
x=sol.reverseBetween(head,left,right)
sol.printLL(x)