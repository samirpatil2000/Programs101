from collections import deque

a=[i for i in range(10**3)]
b=deque(a)
c=len(a)



from sys import getsizeof

print(getsizeof(a),getsizeof(b),getsizeof(a)-getsizeof(b))

print(a)
print(b)