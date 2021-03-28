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


def midElement(head):
    sptr=head
    fptr=head
    l_count=0
    while(fptr and fptr.next):
        sptr=sptr.next
        fptr=fptr.next.next
        l_count+=2
    if(fptr):
        l_count+=1
    return sptr,l_count
        

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


def isPalindrome(head):
    if(head==None or head.next==None):
        return head
    mid_,len_=midElement(head)
    if(len_%2!=0):
        mid_=mid_.next
        len_-=1
    head_2=reverseList(mid_)
    printLinkedList(head_2)
    printLinkedList(head)
    i=0
    ptr_1=head
    ptr_2=head_2
    while(i<=len_ and ptr_2):
        if(ptr_1.val!=ptr_2.val):
            return False
        i+=1
        ptr_1=ptr_1.next
        ptr_2=ptr_2.next
    return True


        







linkedListA=LinkedList()
head = [1,2,3,2,1]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

# x=reverseList(linkedListA.head)
# printLinkedList(x)
# print(midElement(linkedListA.head))

print(isPalindrome(linkedListA.head))


