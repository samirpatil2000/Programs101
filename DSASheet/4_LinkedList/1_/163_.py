class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
        temp=self.head
        while(temp.next and temp.next != self.head):
            print(str(temp.data)+"->",end=" ")
            temp=temp.next
        print(str(temp.data))
        print("\n")
    def addNodeToLinkedList(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            temp=new_node
        else:
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            
def lastNode(head):
        ptr=head
        while(ptr and ptr.next):
            ptr=ptr.next
        return ptr
    
def lenLL(head):
    ptr=head
    count=0
    while(ptr):
        count+=1
        ptr=ptr.next
    return count
            

linkedList=LinkedList()
linkedList.head=newNode(10)
linkedList.addNodeToLinkedList(1)
linkedList.addNodeToLinkedList(3)
linkedList.addNodeToLinkedList(6)
linkedList.addNodeToLinkedList(8)
linkedList.printLinkedList()

# print(linkedList.lenLL())
# print(linkedList.lastNode().data)


def rotateLinkedList(head,k):
    last=lastNode(head)
    lenght=lenLL(head)
    ptr=head
    last.next=head
    while(k>=5):
        k=k%5
    k=lenght-k
    print(k)
    while(k>1):
        ptr=ptr.next
        k-=1
    print(ptr.data)
    head=ptr.next
    ptr.next=None
    return head
new_ll=LinkedList()
new_ll.head=rotateLinkedList(linkedList.head,3)
new_ll.printLinkedList()

    
    



