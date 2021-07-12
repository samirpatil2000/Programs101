
class PriorityQueue:
    
    def __init__(self):
        self.queue=[]
        
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])
    
    def isEmpty(self): 
        return len(self.queue) == 0
    
    def insert(self, data): 
        self.queue.append(data) 
        
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i][1] < self.queue[max][1]: 
                    max = i 
            item = self.queue[max]
            del(self.queue[max])
            return item 
        except IndexError: 
            print() 
            exit() 
    

my_queue=PriorityQueue()
my_queue.insert(["SM",20])
my_queue.insert(["MD",21])
my_queue.insert(["M",22])
my_queue.insert(["S",19])
print(my_queue)


# print(my_queue.delete())
# print(my_queue)

while not my_queue.isEmpty(): 
    print(my_queue.delete()) 