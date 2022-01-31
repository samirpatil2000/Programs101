import time 
import threading

start = time.perf_counter()

def do_something():
    print("Sleeping 1 seconds")
    time.sleep(1)
    print('Done sleeping\n')
    
# do_something()
# do_something() 
# do_something()

'''
    t2=threading.Thread(target=do_something)  # they are not runnnig
    t3=threading.Thread(target=do_something) 
    
    t2.start()
    t3.start()
    
    t2.join()
    t3.join()   # to in that tread before ending the script
'''

threads=[]

for _ in range(10):
    t1 = threading.Thread(target=do_something)
    t1.start()
    threads.append(t1)


for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finish in {round(finish-start,2)} second(s)')
