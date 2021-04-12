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


    

def getDecimalValue(head):
    ptr=head
    str_=""
    while(ptr):
        str_+=str(ptr.val)
        ptr=ptr.next
    print(str_)
    n=len(str_)
    i=n-1
    sum_=0
    while(i>=0):
        # print(2**i,int(str_[n-1-i]))
        x=(2**i)*int(str_[n-1-i])
        sum_+=x
        i-=1
        
    return sum_
        
    





linkedListA=LinkedList()
head = [1,1,1,0,1,0,1,0]
linkedListA.head=newNode(head[0])
for i in head[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()



print(getDecimalValue(linkedListA.head))


# print(2**7)
