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



def removeElements(head,val):
    ptr=head
    preptr=ptr
    while(ptr):
        if(ptr.data==val):
            if(ptr==head):
                ptr=ptr.next
                preptr=ptr
                head=ptr
            else:
                preptr.next=ptr.next
                ptr=ptr.next
        else:
            preptr=ptr
            ptr=ptr.next
    return head

        


linkedListA=LinkedList()
head = [7,7,7,7]
val = 7
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=removeElements(linkedListA.head,val)
print(x)
printLinkedList(x)
    
        
