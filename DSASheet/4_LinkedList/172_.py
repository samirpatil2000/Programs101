class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
        temp=self.head
        while(temp and temp.next):
            print(str(temp.data)+"->",end="")
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



def printLinkedList(head):
    temp=head
    while(temp and temp.next):
        print(str(temp.data)+"->",end="")
        temp=temp.next
    print(str(temp.data))
    print("\n")
    
    
    
def deleteNode(head):
    ptr=head
    preptr=ptr
    while(ptr and ptr.next):
        if(ptr.data < ptr.next.data):
            if(ptr==head):
                preptr=preptr.next
                head=preptr
                ptr=ptr.next
            else:
                preptr.next=ptr.next
                ptr=ptr.next
        else:
            preptr=ptr
            ptr=ptr.next
    return head

linkedListA=LinkedList()
#12->15->10->11->5->6->2->3

list=[12,15,10,11,5,6,2,3]
# list=[10,20,30,40,50,60]
linkedListA.head=newNode(list[0])
for i in list[1:]:
    linkedListA.addNodeToLinkedList(i)


linkedListA.printLinkedList()
x=deleteNode(linkedListA.head)
printLinkedList(x)







    
    
    



