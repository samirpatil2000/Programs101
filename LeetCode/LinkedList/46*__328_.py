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


def lastNode(head):
    fptr=head
    count=0
    while(fptr and fptr.next):
        fptr=fptr.next
        count+=1
    return fptr,count+1



def oddEvenList(head):
    if(head==None and head.next==None):
        return head
    preptr=head
    ptr=head.next
    last,len_=lastNode(head)
    print(len_)
    if(len_%2!=0):
        len_=len_-1
    len_=len_//2
    count=1
    while(ptr and ptr.next and count<=len_):
        printLinkedList(head)
        temp=ptr
        ptr=ptr.next
        preptr.next=ptr
        last.next=temp
        last=temp
        last.next=None
        preptr=preptr.next
        print(preptr.val,ptr.val)
        ptr=ptr.next
        count+=1
    return head
    
def oddEvenList2(head: newNode) -> newNode:
    if(head==None or head.next==None or head.next.next==None):
        return head
    oddIt=head
    evenIt=head.next
    
    
    evenHead=evenIt
    while oddIt.next and evenIt.next:
        
        oddNext=evenIt.next
        oddIt.next=oddNext
        oddIt=oddIt.next
        
        if oddIt:
            evenIt.next=oddIt.next
            evenIt=evenIt.next
    oddIt.next=evenHead
    return head

    




head=[1,2,3,4,5] #[1,3,5,2,4]

linkedListA=LinkedList()
# head = [2,1,3,5,6,4,7] #[2,3,6,7,1,5,4]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=oddEvenList2(linkedListA.head)
printLinkedList(x)

# print(lastNode(linkedListA.head).val)



