# Definition for singly-linked list.
from typing import List


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
    def totalNodes(self,head):
        temp=head
        count_=0
        while temp and temp.next:
            temp=temp.next
            count_+=1
        return count_+1
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head==None or k==1:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        totalnodes=self.totalNodes(head)
        curr=head
        next=ListNode(0)
        prev=dummy
        
        while totalnodes>=k:
            curr=prev.next
            next=curr.next
            
            for _ in range(1,k):
                curr.next=next.next
                next.next=prev.next
                prev.next=next
                next=curr.next
            
            prev=curr
            totalnodes-=k
        return dummy.next
    
    
sol=Solution()

head=[1,2]
head = [1,2,3,4,5]
k = 3
head=sol.makeLL(head)
sol.printLL(sol.reverseKGroup(head,k))                