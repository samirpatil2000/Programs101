class newNode:
    
    def __init__(self,value):
        self.data=value
        self.next=None

class Queue:
    
    def __init__(self):
        self.front=self.rear=None
        
    def isEmpty(self):
        return self.rear==None
        
    def __str__(self):
        current=self.front
        out=""
        while(current!=self.rear):
            out+=str(current.data)+"->"
            current=current.next
        return out[:-2]
    
    def enQueue(self,data):
        temp=newNode(data)    
        if self.rear==None:
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear=temp
    
    def deQueue(self):
        if self.isEmpty(self):
            return
        temp = self.front
        self.front=self.front.next
        if(self.front==None):
            self.rear=None
        return temp.value
    
    
        
    