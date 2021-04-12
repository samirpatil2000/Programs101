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



def deleteDuplicates(head):
    ptr=head
    preptr=ptr
    while(ptr and ptr.next):
        if(ptr.data==ptr.next.data):
            while(ptr and ptr.next and ptr.data==ptr.next.data):
                ptr=ptr.next
            # if(ptr.next==None):
                
            if(preptr==head):
                if(preptr.data!=ptr.data):
                    preptr.next=ptr.next
                    head=preptr
                else:
                    ptr=ptr.next
                    preptr=ptr
                    head=ptr
            elif(ptr.next==None):
                preptr.next=None
                return preptr
            else:
                ptr=ptr.next
                preptr.next=ptr
        else:
            preptr=preptr.next
            ptr=ptr.next
            
    return head


def deleteDuplicates_2(head):
    preptr=newNode(-1)
    preptr.next=head
    ptr=head
    res=preptr
    while(ptr and ptr.next):
        if(ptr.data!=ptr.next.data):
            ptr=ptr.next
            preptr=preptr.next
        else:
            while(ptr and ptr.next and ptr.data==ptr.next.data):
                ptr=ptr.next
            ptr=ptr.next
            preptr.next=ptr
    return res.next
        


linkedListA=LinkedList()
head = [-1,0,0,0,0,3,3]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=deleteDuplicates_2(linkedListA.head)
printLinkedList(x)
    
        
