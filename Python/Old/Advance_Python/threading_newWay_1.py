import time 
import concurrent.futures

start = time.perf_counter()

def do_something(second):
    print(f"Sleeping {second} second(s)\n")
    time.sleep(second)
    return 'Done sleeping \n'

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1=executor.submit(do_something,5)
    f2=executor.submit(do_something,5)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()

print(f'Finish in {round(finish-start,2)} second(s)')
