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


def reverseList(head):
    
    preptr=head
    ptr=head.next
    new_node=None
    while(ptr):
        # printLinkedList(head)
        preptr.next=new_node
        new_node=preptr
        preptr=ptr
        ptr=ptr.next
    preptr.next=new_node
    new_node=preptr
    head=new_node
    return head

def reverseList_2(head):
    
    ptr=head.next
    new_node=None
    while(head and head.next):
        # printLinkedList(head)
        head.next=new_node
        new_node=head
        head=ptr
        ptr=ptr.next
    head=new_node
    return head






linkedListA=LinkedList()
head = [1,2,3]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=reverseList_2(linkedListA.head)
printLinkedList(x)
    
        
