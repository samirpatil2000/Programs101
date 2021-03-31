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

def addTwoNumbers(headA,headB):
    headC=newNode(-1)
    ptr_1=reverseList(headA)
    ptr_2=reverseList(headB)
    
    printLinkedList(ptr_1)
    printLinkedList(ptr_2)
    ptr_3=headC
    while(ptr_1 and ptr_2):
        sum_=ptr_1.val+ptr_2.val
        if(ptr_3.next):
            ptr_3=ptr_3.next
            ptr_3.val+=sum_%10
        else:
            ptr_3.next=newNode(sum_%10)
            ptr_3=ptr_3.next
            
        ptr_1=ptr_1.next
        ptr_2=ptr_2.next
        if(sum_>9):
            ptr_3.next=newNode(1)
                
    if(ptr_1):
        if(ptr_1.val==10):
            ptr_3.next=newNode(0)
            ptr_3=ptr_3.next
            ptr_3.next=newNode(1)
            ptr_3=ptr_3.next
        else:
            ptr_3.next=ptr_1
    elif(ptr_2):
        if(ptr_2.val==10):
            ptr_3.next=newNode(0)
            ptr_3=ptr_3.next
            ptr_3.next=newNode(1)
            ptr_3=ptr_3.next
        else:
            ptr_3.next=ptr_2
    result=reverseList(headC.next)
    return result




        
        
    
    
    



linkedListA=LinkedList()
headA = [1]
linkedListA.head=newNode(headA[0])
for i in headA[1:]:
    linkedListA.addNodeToLinkedList(i)
# linkedListA.printLinkedList()



linkedListB=LinkedList()
headB = [9,9,9]
linkedListB.head=newNode(headB[0])
for i in headB[1:]:
    linkedListB.addNodeToLinkedList(i)
# linkedListB.printLinkedList()

x=addTwoNumbers(linkedListA.head,linkedListB.head)
printLinkedList(x)
