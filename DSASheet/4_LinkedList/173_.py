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

def segregate(head,N):
    ptr=head
    preptr=ptr
    last_node=lastNode(head)
    count=0
    while(ptr and ptr.next and count<N):
        if(ptr.data % 2!=0):
            temp=ptr
            if(ptr==head):
                ptr=ptr.next
                preptr=ptr
                head=ptr
            else:
                preptr.next=ptr.next
                ptr=ptr.next
   
            last_node.next=temp
            last_node=temp
            temp.next=None
            last_node.next=None
        else:
            preptr=ptr
            ptr=ptr.next
        count+=1
    return head



    
    
    




linkedListA=LinkedList()

list=[17 , 15 , 8 , 9 , 2 , 4 , 6]
N=7

linkedListA.head=newNode(list[0])
for i in list[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=segregate(linkedListA.head,N)
printLinkedList(x)
# printLinkedList(linkedListA.head)






    
    
    



  
    







    
    
    



