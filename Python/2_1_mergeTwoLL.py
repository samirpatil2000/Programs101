class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printLinkedList(self):
        temp=self.head
        while(temp!=None):
            print(str(temp.data)+"->",end="")
            temp=temp.next
        print("\n")
    def addNodeToLast(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            temp=new_node
            return
        while(temp.next):
            temp=temp.next
        temp.next=new_node

def creationOfLinkedList(head):
    num=int(input("Enter the number (-1 for end) : "))
    while(num != -1):
        if (head is None):
            head=newNode(num)
        else:
            ptr=head
            while(ptr.next):
                ptr=ptr.next
            new=newNode(num)
            ptr.next=new
        num=int(input("Enter the number (-1 for end) : "))
    return head


def mergeTwoLinkedList(la,lb):
    head1=la.head
    head2=lb.head
    # newLL=LinkedList()
    newLL=newNode(0)
    # head3=newLL.head
    tail=newLL
    
    while(head1 != None and head2 != None):
        if(head1.data > head2.data):
            # newLL.addNodeToLast(head2.data)
            tail.next=head2
            head2=head2.next
        else:
            # newLL.addNodeToLast(head1.data)
            tail.next=head1
            head1=head1.next
        tail=tail.next
    if(head1 !=None):
        # while(head1 != None):
            # newLL.addNodeToLast(head1.data)
        tail.next=head1
        # head1=head1.next
        # tail=tail.next
    if(head2 !=None):
        # while(head2 != None):
            # newLL.addNodeToLast(head2.data)
        tail.next=head2
        # head2=head2.next
        # tail=tail.next
        
    return newLL.next
        


linkedListA=LinkedList()
linkedListB=LinkedList()
linkedListA.head=newNode(1)
linkedListB.head=newNode(1)

creationOfLinkedList(linkedListA.head)
creationOfLinkedList(linkedListB.head)
print("A")
linkedListA.printLinkedList()
print("B")
linkedListB.printLinkedList()
print("Merge List")
linc=LinkedList()
linc.head=mergeTwoLinkedList(linkedListA,linkedListB)
linc.printLinkedList()

