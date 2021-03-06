class newNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp.next):
            print(str(temp.data) + "->",end="")
            temp = temp.next
        print(str(temp.data))
        print();

    def addNodeToLast(self, data):
        new_node = newNode(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
        new_node.prev=temp
        
def reverseLL(head):
    ptr1=head
    ptr2=ptr1.next
    ptr1.next=None   
    ptr1.prev=ptr2 
    while(ptr2):
        ptr2.prev=ptr2.next
        ptr2.next=ptr1
        ptr1=ptr2
        ptr2=ptr2.prev
    head=ptr1
    return head
    
    


linkedListA = LinkedList()
linkedListA.addNodeToLast(3)
linkedListA.addNodeToLast(4)
linkedListA.addNodeToLast(2)
linkedListA.addNodeToLast(7)
linkedListA.addNodeToLast(10)
linkedListA.addNodeToLast(9)
linkedListA.addNodeToLast(11)

print("A")
linkedListA.printLinkedList()
lea=LinkedList()
lea.head=reverseLL(linkedListA.head)
print("Reverse LL")
lea.printLinkedList()




