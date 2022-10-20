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

def reverseLL__II(head:newNode):
    dummy = None
    ptr = head.next
    while ptr:
        head.next=dummy
        dummy=head
        head=ptr
        ptr=ptr.next
    # print(dummy.val,head.val)
    head.next=dummy
    dummy=head
    
    return dummy
    

        

def reverseLL_III(curr:newNode,prev=None):
    if not curr:return prev
    new_head=reverseLL_III(curr.next,curr)
    curr.next=prev
    return new_head





linkedListA=LinkedList()
head = [1,2,3,4,5,6,7,8,9]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

x=reverseLL_III(linkedListA.head)
printLinkedList(x)



