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
   
def insertionSort(head):
    ptr=head.next
    while(ptr and ptr.prev and ptr.next):
        j=ptr.prev
        temp=ptr.data
        while(j and j.data > temp):
            j.next.data=j.data
            j=j.prev
        if(j): 
            j.next.data=temp
        # else:
        #     j.data=temp
        ptr=ptr.next
    return head

def insertionSortDLL(h):
    if h == None:
        return None
    #Make the first node the start of the sorted list.
    sortedList= h
    h=h.next
    sortedList.next= None
    while h != None:
        curr= h
        h=h.next
        if curr.data<sortedList.data:
            #Advance the nodes
            curr.next= sortedList
            sortedList= curr
        else: 
            #Search list for correct position of current.
            search= sortedList
            while search.next!= None and curr.data > search.next.data:
                search= search.next
            #current goes after search.
            curr.next= search.next
            search.next= curr
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
lea=LinkedList()


print("Insertion Sort With Nodes")
lea.head=insertionSortDLL(linkedListA.head)

lea.printLinkedList()




