class newNode:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
        temp=self.head
        while(temp and temp.next):
            print(str(temp.val)+"->",end="")
            temp=temp.next
        print(str(temp.val))
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
    count=0
    ptr=head
    while(ptr and ptr.next):
        ptr=ptr.next
        count+=1
    return count


def printLinkedList(head):
    temp=head
    while(temp and temp.next):
        print(str(temp.val)+"->",end="")
        temp=temp.next
    print(str(temp.val))
    print("\n")


def deleteDuplicates_2(head):
    preptr=newNode(-1)
    preptr.next=head
    ptr=head
    res=preptr
    while(ptr and ptr.next):
        if(ptr.val!=ptr.next.val):
            preptr=ptr
            ptr=ptr.next
        else:
            while(ptr and ptr.next and ptr.val==ptr.next.val):
                ptr=ptr.next
            preptr.next=ptr
    return res.next


linkedListA=LinkedList()
head = [1,1,2,2]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=deleteDuplicates_2(linkedListA.head)
printLinkedList(x)
    
        
