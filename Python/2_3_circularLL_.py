class newNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printLinkedList(self):
        temp=self.head.next
        while(temp.next != self.head):
            print(str(temp.data)+"->",end=" ")
            temp=temp.next
        print(str(temp.data))
        print("\n")
        
    def addNodeToLinkedList(self,data):
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
            

linkedList=LinkedList()
linkedList.head=newNode(10)
linkedList.addNodeToLinkedList(1)
linkedList.addNodeToLinkedList(3)
linkedList.addNodeToLinkedList(6)
linkedList.addNodeToLinkedList(8)
linkedList.printLinkedList()

            
            
            
            
    