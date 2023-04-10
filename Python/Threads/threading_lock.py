import threading
import time


class ThreadCounter:
    
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()
    
    def count(self, thread_no):
        while True:
            self.counter += 1
            self.lock.acquire()
            print(f"{thread_no}: Just increased counter to {self.counter}")
            time.sleep(1)
            print(f"{thread_no}: Done Some work, now value is: {self.counter}")
            self.lock.release()
            
tc = ThreadCounter()

for i in range(5):
    t = threading.Thread(target=tc.count, args=(i, ))
    t.start()
    t.join()
