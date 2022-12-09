class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
        temp=self.head.next
        while(temp.next and temp.next != self.head):
            print(str(temp.data)+"->",end=" ")
            temp=temp.next
        print(str(temp.data))
        print("\n")
        
    def addNodeToLinkedListCircular(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            new_node.next=new_node
            temp=new_node
            return
        else:
            while(temp.next and temp.next != self.head):
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def addNodeToLinkedList(self,data):
        temp=self.head
        new_node=newNode(data)
        if(temp == None):
            temp=new_node
        else:
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            

linkedList=LinkedList()
linkedList.head=newNode(10)
linkedList.addNodeToLinkedListCircular(1)
linkedList.addNodeToLinkedListCircular(3)
linkedList.addNodeToLinkedListCircular(6)
linkedList.addNodeToLinkedListCircular(8)
linkedList.printLinkedList()

linkedListB=LinkedList()
linkedListB.head=newNode(20)
linkedListB.addNodeToLinkedList(32)
linkedListB.addNodeToLinkedList(3)
linkedListB.addNodeToLinkedList(12)
linkedListB.addNodeToLinkedList(42)
linkedListB.printLinkedList()

            
def checkItisCircularLinkedList(list):
    head=list.head
    slow=head
    fast=head
    while(fast.next and fast.next.next):
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            print("It is circular")
            break
    else:
        print("Loop Doesn't Exists")

def removeCircularLoop(list):
    last_node=list.head
    while(last_node.next and last_node.next==last_node):
        last_node=last_node.next
    last_node.next=None
    
    
    
    
print("A")
checkItisCircularLinkedList(linkedList)
print("B")
checkItisCircularLinkedList(linkedListB)
print("Removing the linked list")
removeCircularLoop(linkedList)
print("Checking for loop")
checkItisCircularLinkedList(linkedList)

