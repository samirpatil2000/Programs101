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
            
def lenOFLL(head):
    count=0
    ptr=head
    while(ptr and ptr.next):
        ptr=ptr.next
        count+=1
    count+=1
    return count


def printLinkedList(head):
    temp=head
    while(temp and temp.next):
        print(str(temp.data)+"->",end="")
        temp=temp.next
    print(str(temp.data))
    print("\n")




def swapNodes(head, k):
    k_last=lenOFLL(head)-k-1
    # temp=head
    preptr_1=head
    ptr_1=head
    count=0
    while(ptr_1 and count==k):
        count+=1
        preptr_1=ptr_1
        ptr_1=ptr_1.next
    
    preptr_2=preptr_1
    ptr_2=ptr_1
    while(ptr_2 and count==k_last):
        preptr_2=ptr_2
        ptr_2=ptr_2.next
    
        
    

    
        
    return head
    
        


linkedListA=LinkedList()
head = [1,2,3,4,5]
k=2
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

    
swapNodes(linkedListA.head,k)
        


     