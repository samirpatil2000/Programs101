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



def printLinkedList(head):
    temp=head
    while(temp.next and temp.next != head):
        print(str(temp.data)+"->",end=" ")
        temp=temp.next
    print(str(temp.data))
    print("\n")
    
# {2,2,0,1}

linkedListA=LinkedList()
linkedListA.head=newNode(1)


linkedListA.addNodeToLinkedList(0)
linkedListA.addNodeToLinkedList(1)
linkedListA.addNodeToLinkedList(2)
linkedListA.addNodeToLinkedList(1)

linkedListB=LinkedList()
linkedListB.head=newNode(1)
linkedListB.addNodeToLinkedList(0)
linkedListB.addNodeToLinkedList(1)

linkedListA.printLinkedList()
linkedListB.printLinkedList()
    

def LL(root):
    ptr=root
    list=[]
    while(ptr):
        list.append(ptr.data)
        ptr=ptr.next
    return list

def makeListTONumber(list_):
    str_=""
    for i in list_:
        str_+=str(i)
    return int(str_)

def multiplication(headA,headB):
    num_a=makeListTONumber(LL(headA))
    num_b=makeListTONumber(LL(headB))
    return num_a,num_b,num_a*num_b

print(multiplication(linkedListA.head,linkedListB.head))
        
    



    
    
    



