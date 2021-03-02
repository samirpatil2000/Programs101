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
            print(str(temp.data)+"->")
            temp=temp.next
        
linkedList=LinkedList()
linkedList.head=newNode(1)

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

creationOfLinkedList(linkedList.head)

linkedList.printLinkedList()

    