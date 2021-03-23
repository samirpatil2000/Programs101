class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.bottom=None
        
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


    

def mergeTwoLinkedList(la,lb):
    head1=la
    head2=lb
    newLL=newNode(0)
    tail=newLL
    
    while(head1 != None and head2 != None):
        if(head1.data > head2.data):
            tail.bottom=head2
            head2=head2.bottom
        else:
            tail.bottom=head1
            head1=head1.bottom
            
        tail=tail.bottom
    if(head1 !=None):
        tail.bottom=head1
    else:
        tail.bottom=head2
    return newLL.bottom


def flatten(root):
    if(root==None or root.next==None):
        return root
    root.next=flatten(root.next)
    root=mergeTwoLinkedList(root,root.next)
    return root
            



    
    



