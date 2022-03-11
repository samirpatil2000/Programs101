# Definition for singly-linked list.
from collections import defaultdict
from curses import noecho
from email.policy import default
from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        
    
class Solution:
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        hash_ = defaultdict(list)
        queue = []
        for _head in lists:
            if _head:
                hash_[_head.val].append(_head)
                queue.append(_head.val)
        heapq.heapify(queue)
        curr = head
        while queue:
            val = heapq.heappop(queue)
            print(val)
            node = None
            if hash_[val]:
                node = hash_[val].pop()
            curr.next = node
            curr = curr.next
            if node and node.next:
                hash_[node.next.val].append(node.next)
                heapq.heappush(queue, node.next.val)
        return head.next

            
        
sol = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]

lists = [[]]
for i in range(len(lists)):
    lists[i] = sol.makeLL(lists[i])

sol.printLL(sol.mergeKLists(lists))

