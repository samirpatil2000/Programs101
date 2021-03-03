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
        
    def addNodeToLinkedListCircular(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            new_node.next=new_node
            temp=new_node
            return
        else:
            while(temp.next and temp.next != self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def addNodeToLinkedList(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            temp=new_node
        else:
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            

linkedList=LinkedList()
linkedList.head=newNode(10)
linkedList.addNodeToLinkedListCircular(1)
linkedList.addNodeToLinkedListCircular(3)
linkedList.addNodeToLinkedListCircular(6)
linkedList.addNodeToLinkedListCircular(8)
linkedList.printLinkedList()

def printLinked_List(head,tail):
    ptr=head
    while(ptr and ptr !=tail):
        print(str(ptr.data)+"->",end=" ")
        ptr=ptr.next
    print(str(ptr.data))
    print("\n")
        
        
    
    
    
            
def splitLinkedLIst(list):
    head=list.head
    slow=head
    fast=head
    while(fast.next and fast.next.next and fast.next !=head):
        slow=slow.next
        fast=fast.next.next
    ptr=slow
    # slow.next=None
    print("First Half")
    printLinked_List(head,ptr)
    print("Second Half")
    printLinked_List(ptr.next,fast)
    
    
    
    
    
    
print("A")
splitLinkedLIst(linkedList)


