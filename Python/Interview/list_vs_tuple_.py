a=[i for i in range(10**6)]
b=tuple(a)
c=len(a)

from sys import getsizeof
print("c",c,getsizeof(c))
print(getsizeof(a),getsizeof(b),getsizeof(a)-getsizeof(b))

x=[16,16,64,976,7576,24416,697416]
x=[(x[i]//8,x[i]%8) for i in range(len(x))]
print(x)