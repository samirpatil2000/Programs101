

class Stack:
    
    
    def __init__(self) -> None:
        self.queue1 = []
        self.queue2 = []
    
    
    def pop(self):
        if not self.queue2: 
            print("Underflow")
            return 
        self.queue2.pop(0)
        
    
    def push(self, n):
        self.queue1 = [n] + self.queue2
        self.queue2 = self.queue1
        self.queue1 = []
        # print(self.queue2)
        
        # with using only one queue
        
        # self.queue2.append(n)
        # n = len(self.queue2) - 1
        # while n:
        #     n -= 1
        #     self.queue2.append(self.queue2.pop(0))
        
        return
    


import time

t1 = time.time()
st = Stack()
for i in range(2, 5000):
    st.push(i)
    
    
st.pop()
for i in [6, 7, 8]:
    st.push(i)

# print(st.queue2)

print("Time : ", time.time() - t1)
# n = 1
# while n:
#     n = int(input("Enter the value \n 0. Exit \n 1. push \n 2. pop \n :"))
#     if n == 1:
#         st.push(int(input("Enter the value : ")))
#     elif n == 2:
#         st.pop()
#     else:
#         n = 0
#         break
