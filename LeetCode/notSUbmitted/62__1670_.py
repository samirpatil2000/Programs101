from typing import NoReturn
# timelimit for push last and middle

class Node():
    def __init__(self,val):
        self.val=val
        self.next=None

class FrontMiddleBackQueue:
    
    def __init__(self):
        self.head=None
    
    def printLinkedList(self):
        if(self.head==None):
            return print("[]")
        temp=self.head
        while(temp and temp.next):
            print(str(temp.val)+"->",end="")
            temp=temp.next
        print(str(temp.val)+" -< ")
        print("\n")

    def pushFront(self, val: int) -> None:
        new_node=Node(val)
        if(self.head==None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            

    def pushMiddle(self, val: int) -> None:
        new_node=Node(val)
        if(self.head==None):
            self.head=new_node
        else:
            sptr=self.head
            prev_sptr=sptr
            fptr=self.head
            while(fptr and fptr.next):
                prev_sptr=sptr
                sptr=sptr.next
                fptr=fptr.next.next
            prev_sptr.next=new_node
            new_node.next=sptr
    
    
        

    def pushBack(self, val: int) -> None:
        new_node=Node(val)
        if(self.head==None):
            self.head=new_node
        else:
            ptr=self.head
            while(ptr and ptr.next):
                ptr=ptr.next
            ptr.next=new_node
        

    def popFront(self) -> int:
        if(self.head==None):
            return -1
        else:
            ptr=self.head.val
            self.head=self.head.next
            return ptr
            

    def popMiddle(self) -> int:
        if(self.head==None):
            return -1
        elif(self.head.next==None):
            temp=self.head.val
            self.head=None
            return temp
        else:
            sptr=self.head
            prev_sptr=sptr
            fptr=self.head
            while(fptr and fptr.next and fptr.next.next):
                prev_sptr=sptr
                sptr=sptr.next
                fptr=fptr.next.next
                
            temp=sptr.val
            if(fptr==self.head):
                self.head=self.head.next
                # prev_sptr.next=None
            else:
                prev_sptr.next=sptr.next
            del sptr
            return temp

    def popBack(self) -> int:
        if(self.head==None):
            return -1
        elif(self.head.next==None):
            temp=self.head.val
            self.head=None
            return temp
        else:
            ptr=self.head
            prev=ptr
            while(ptr and ptr.next):
                prev=ptr
                ptr=ptr.next
            prev.next=None
            temp=ptr.val
            del ptr
            return temp
            


q=FrontMiddleBackQueue()

# head = [1]
# q.head=Node(head[0])
# for i in head[1:]:
#     q.pushFront(i)

# q.printLinkedList()   
# x=q.popMiddle()
# # print(x)
# q.printLinkedList()

q.pushFront(1)   #// [1]
q.printLinkedList()
q.pushBack(2)    #// [1, 2]
q.printLinkedList()
q.pushMiddle(3)  #// [1, 3, 2]
q.printLinkedList()
q.pushMiddle(4)  #// [1, 4, 3, 2]
q.printLinkedList()
q.popFront()     #// return 1 -> [4, 3, 2]
q.printLinkedList()
q.popMiddle()    #// return 3 -> [4, 2]
q.printLinkedList()
q.popMiddle()    #// return 4 -> [2]
q.printLinkedList()
print(q.popBack())      #// return 2 -> []
print(q.popFront())     #// return -1 -> [] (The queue is empty)
q.printLinkedList()
