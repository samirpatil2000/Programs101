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
    count=0
    ptr=head
    while(ptr and ptr.next):
        ptr=ptr.next
        count+=1
    return count


def printLinkedList(head):
    temp=head
    while(temp and temp.next):
        print(str(temp.data)+"->",end="")
        temp=temp.next
    print(str(temp.data))
    print("\n")




linkedListA=LinkedList()
linkedListB=LinkedList()
list1 = [0,1,2,3,4,5,6]
a = 2
b = 5
list2 = [1000000,1000001,1000002,1000003,1000004]

linkedListA.head=newNode(list1[0])
for i in list1[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()


linkedListB.head=newNode(list2[0])
for i in list2[1:]:
    linkedListB.addNodeToLinkedList(i)
linkedListB.printLinkedList()


def mergeInBetween(list1, a, b, list2):
    i=0
    head1=list1
    new_head=head1
    ptr1=None
    ptr2=None

    while(i<=b):
        if(i==a-1):
            ptr1=head1
        if(i==b):
            ptr2=head1.next
            break
        head1=head1.next
        i+=1
    ptr1.next=list2    
    temp=list2
    while(temp and temp.next):
        temp=temp.next
    temp.next=ptr2
    return new_head

x=mergeInBetween(linkedListA.head,a,b,linkedListB.head)
printLinkedList(x)
    
        
