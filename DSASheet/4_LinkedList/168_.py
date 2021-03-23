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

linkedList=LinkedList()
linkedList.head=newNode(1)

linkedList.addNodeToLinkedList(0)
linkedList.addNodeToLinkedList(1)
linkedList.addNodeToLinkedList(2)
linkedList.addNodeToLinkedList(1)
linkedList.addNodeToLinkedList(0)
linkedList.addNodeToLinkedList(1)
linkedList.addNodeToLinkedList(2)
linkedList.addNodeToLinkedList(1)
linkedList.printLinkedList()


#interchanging values
def function(root):
    ptr=root
    preptr=ptr
    last=lastNode(root)
    count=0
    while(ptr and ptr.next and count < 15):
        print(ptr.data,preptr.data )
        if(ptr.data==2):
            last.next=newNode(2)
            last=last.next
            if(ptr==root):
                ptr=ptr.next
                root=ptr
            else:
                preptr.next=ptr.next
                ptr=ptr.next
        elif(ptr.data==0):
            if(root==ptr):
                preptr=ptr
                ptr=ptr.next
            else:
                new_node=newNode(0)
                new_node.next=root
                root=new_node
                preptr.next=ptr.next
                ptr=ptr.next
        else:
            preptr=ptr
            ptr=ptr.next
        count+=1
        printLinkedList(root)
    return root

            


#interchnaging nodes
def function_(root):
    ptr=root
    preptr=ptr
    last=lastNode(root)
    count=0
    while(ptr and ptr.next and count<15):
        print(ptr.data,preptr.data)
        if(ptr.data==2):
            temp=ptr
            ptr=ptr.next
            
            last.next=temp
            temp.next=None
            last=last.next            
            if(ptr==root):
                root=ptr
                preptr=ptr
            else:
                preptr.next=ptr
                
        elif(ptr.data==0):
            if(root==ptr):
                preptr=ptr
                ptr=ptr.next
                
            else:
                temp=ptr
                ptr=ptr.next
                preptr.next=ptr
                temp.next=root
                root=temp
                
        else:
            preptr=ptr
            ptr=ptr.next
        count+=1
        printLinkedList(root)
    return root

            
x=function_(linkedList.head)
printLinkedList(x)  

    
                
    
    
    



