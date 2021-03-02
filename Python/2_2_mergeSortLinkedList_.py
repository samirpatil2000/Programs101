class newNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head
        while (temp != None):
            print(str(temp.data) + "->",end="")
            temp = temp.next
        print("\n");

    def addNodeToLast(self, data):
        new_node = newNode(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node



def mergeTwoLinkedList(la,lb):
    
    head1 = la.head
    head2 = lb.head
    newLL=LinkedList()

    while (head1 != None and head2 != None):
        if (head1.data > head2.data):
            newLL.addNodeToLast(head2.data)
            head2 = head2.next
        else:
            newLL.addNodeToLast(head1.data)
            head1 = head1.next
    if (head1 != None):
        while (head1 != None):
            newLL.addNodeToLast(head1.data)
            head1 = head1.next
    if (head2 != None):
        while (head2 != None):
            newLL.addNodeToLast(head2.data)
            head2 = head2.next
    return newLL


def findMidNode(head,tail):
    fast=head
    slow=head
    while(fast!=tail and fast.next!=tail):
        fast=fast.next.next
        slow=slow.next
    return slow

def tailNode(head):
    temp=head
    while(temp.next != None):
        temp=temp.next
    return temp


def mergeSort(head,tail):
    if(head == tail):
        list_=LinkedList()
        list_.addNodeToLast(head.data)
        return list_
    mid=findMidNode(head,tail)
    firstSortedList=mergeSort(head,mid)
    secondSortedList=mergeSort(mid.next,tail)
    sortedList=mergeTwoLinkedList(firstSortedList,secondSortedList)
    return sortedList

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

print("Sorted List")
tail=tailNode(linkedListA.head)
print(findMidNode(linkedListA.head,tail).data)
li=mergeSort(linkedListA.head,tail)
li.printLinkedList()



