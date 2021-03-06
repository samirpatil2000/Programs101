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


def countTriplets(head,X):
    i=head
    counter=0
    last=lastNode(head)
    
    while(i.next.next.next):
        low=i.next
        high=last
        while(low and high and low !=high):
            sum=i.data+low.data+high.data
            if(sum==X):
                counter+=1
                print(i.data,low.data,high.data)
                low=low.next
                high=high.prev
            else:
                if(sum<X):
                    low=low.next
                else:
                    high=high.prev
        i=i.next
    
    return counter
    
    
    
    

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

print("The triplet is = ",countTriplets(linkedListA.head,17))

