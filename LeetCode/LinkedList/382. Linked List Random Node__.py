# Definition for singly-linked list.
from typing import Optional
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        result=-1
        t=self.head
        i=1
        while t:
            if random.randint(1,i)==i-1:
                result=t.val
            t=t.next
            i+=1
        return result 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()