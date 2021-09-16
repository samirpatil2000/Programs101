class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):self.head=None
    def createHash(self,maxElement):
        hashset=set()
        prev = 0
        curr = 1
        hashset.add(prev)
        hashset.add(curr)
        while (curr <= maxElement):
            temp = curr + prev
            hashset.add(temp)
            prev = curr
            curr = temp
        return hashset
    def main(self,arr):
        maxElement=max(arr)
        if not arr:return None
        hashset=self.createHash(maxElement)
        head=newNode(-1)
        ptr=head
        for i in arr:
            if i not in hashset:
                ptr.next=newNode(i)
                ptr=ptr.next
        return head.next
    
import sys

def get_ints(): 
    return list(map(int, sys.stdin.readline().strip().split()))

t=int(input())
arr=get_ints()               
ll=LinkedList()
print(ll.main(arr))