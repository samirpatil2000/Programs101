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
        
def lastNode(head):
    if(head.next==None):
        return head
    return lastNode(head.next)

def findSumPair(head,x):
    low=head
    high=lastNode(head)
    while(low and high and low != high):
        sum=low.data+high.data
        if(sum==x):
            print(low.data,",",high.data)
            low=low.next
            high=high.prev
        else:
            if(sum>x):
                high=high.prev
            else:
                low=low.next
    
    
    

linkedListA = LinkedList()
linkedListA.addNodeToLast(1)
linkedListA.addNodeToLast(2)
linkedListA.addNodeToLast(4)
linkedListA.addNodeToLast(5)
linkedListA.addNodeToLast(6)
linkedListA.addNodeToLast(8)
linkedListA.addNodeToLast(9)







print("A")
linkedListA.printLinkedList()

findSumPair(linkedListA.head,7)
# print(lastNode(linkedListA.head).data)


