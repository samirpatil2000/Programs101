import threading
import time

ls = []
def func(number):
    print(f"Ran {number}")
    time.sleep(1)
    print(f"Done {number}")
    

def counter(n, a):
    for i in range(1, n + 1):
        ls.append(str(i) + "-" +  str(a))
        time.sleep(0.5)
        
    

# x = threading.Thread(target=func, args=(1, ))
# x.start()
# y = threading.Thread(target=func, args=(2, ))
# y.start()
# x.join()
# y.join()


x = threading.Thread(target=counter, args=(5, "x"))
x.start()

y = threading.Thread(target=counter, args=(5, "y"))
y.start()
x.join() 
y.join()
print(ls)
print(f"Active threads = {threading.active_count()}")
