# Definition for singly-linked list.
from typing import List

def get_length(root):
    ans = 0
    while root is not None:
        root = root.next
        ans += 1
    return ans 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def makeList(self,list_):
        head=ListNode(list_[0])
        temp=head
        for i in list_[1:]:
            temp.next=ListNode(i)
            temp=temp.next
        return head
    
    def printList(self,head):
        temp=head
        while temp:
            print(temp.val,end=" ")
            temp=temp.next
        print()
        
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        result=[None]*k
        length=get_length(head)
        current=head
        for i in range(k):
            num_element=(length//k)+(1 if i < (length%k) else 0)
            for j in range(num_element):
                if j==0:
                    result[i]=current
                    
                if j==num_element-1:
                    temp=current.next
                    current.next=None
                    current=temp
                else:
                    current=current.next
        return result
    
sol=Solution()

list_= [1,2,3]
k = 5

head=sol.makeList(list_)
print(sol.printList(head))
print(x:=sol.splitListToParts(head,k))

for i in x:
    sol.printList(i)
