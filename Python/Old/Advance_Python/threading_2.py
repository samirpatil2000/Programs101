import time 
import threading

"""  FUNCTION TAKING ARGUMENT  """

start = time.perf_counter()

def do_something(second):
    print(f"Sleeping {second} second(s)")
    time.sleep(second)
    print('Done sleeping\n')


threads=[]

for _ in range(10):
    t1 = threading.Thread(target=do_something,args=[1.5])
    t1.start()
    threads.append(t1)


for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finish in {round(finish-start,2)} second(s)')
