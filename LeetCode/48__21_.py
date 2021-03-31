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

def printLinkedList(head):
    temp=head
    while(temp and temp.next):
        print(str(temp.val)+"->",end="")
        temp=temp.next
    print(str(temp.val))
    print("\n")


    

def mergeTwoLL(l1,l2):
    ptr_3=newNode(-1)
    res=ptr_3
    while(l1 and l2):
        if(l1.val>l2.val):
            ptr_3.next=l2
            l2=l2.next
        else:
            ptr_3.next=l1
            l1=l1.next
        ptr_3=ptr_3.next
        
        
    if(l1):
        ptr_3.next=l1
    else:
        ptr_3.next=l2
    return res.next


                
                            
    





linkedListA=LinkedList()
list_1 = [2,4,6,8]
linkedListA.head=newNode(list_1[0])
for i in list_1[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

linkedListB=LinkedList()
list_2 = [3,5,6,7,8,9]
linkedListB.head=newNode(list_2[0])
for i in list_2[1:]:
    linkedListB.addNodeToLinkedList(i)
linkedListB.printLinkedList()




# print(2**7)
x=mergeTwoLL(linkedListA.head,linkedListB.head)
printLinkedList(x)