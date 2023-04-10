import threading
import time
from concurrent.futures import ThreadPoolExecutor


def worker(number):
    print("Calculating the results for number => " + str(number))
    time.sleep(2)
    return number ** 2
    

pool = ThreadPoolExecutor(10)
# for i in range(6): 
#     result1 = pool.submit(worker, i)
pool.map(worker, range(20))
# result2 = pool.submit(worker, 2)
# result3 = pool.submit(worker, 3)
# result4 = pool.submit(worker, 4)
# result5 = pool.submit(worker, 5)
# result6 = pool.submit(worker, 6)

