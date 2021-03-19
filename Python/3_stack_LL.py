class newNode:
    
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    
    def __init__(self):
        self.top=newNode("Head")
        self.size=0
    def __str__(self):
        cur = self.top.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    
    def peek(self):
        
        if self.isEmpty():
            raise Exception("EmptyStack")
        return self.top.next.value
    
    def push(self,value):
        node=newNode(value)
        node.next=self.top.next
        self.top.next=node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("EmptyStack")
        remove=self.top.next
        self.top.next=self.top.next.next
        self.size-=1
        return remove.value

stack=Stack()   
for i in range(1, 11):
    stack.push(i)
print(stack)
 
for _ in range(1, 6):
    remove = stack.pop()
    print(remove)
print(stack)
