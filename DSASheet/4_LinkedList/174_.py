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



def NTHNode(head,N):
    temp=head
    len_ll=lastNode(head)
    count=0
    if(N>=len_ll):
        return -1
    while(temp and temp.next and count<=len_ll-N):
        temp=temp.next
        count+=1
    return temp.data

                
    
    
    




linkedListA=LinkedList()

list=[17 , 15 , 8 , 9 , 2 , 4 , 6]
N=23

linkedListA.head=newNode(list[0])
for i in list[1:]:
    linkedListA.addNodeToLinkedList(i)
linkedListA.printLinkedList()

print(NTHNode(linkedListA.head,N))







    
    
    



  
    







    
    
    



