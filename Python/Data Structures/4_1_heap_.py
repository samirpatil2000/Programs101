import heapq




def sol():
    q=[(-2,3)]
    heapq.heapify(q)
    heapq.heappush(q,(-3,4))
    heapq.heappush(q,(-40,43))
    heapq.heappush(q,(-89,43))
    heapq.heappush(q,(-43,0))
    heapq.heappush(q,(-43,0))
    arr=[]
    while q:
        x=heapq.heappop(q)
        arr.append((-x[0],x[1]))
        # print(x)
        
    print(arr)

sol()
def sol():
    q=[(2,3)]
    heapq.heapify(q)
    heapq.heappush(q,(3,4))
    heapq.heappush(q,(40,43))
    heapq.heappush(q,(89,43))
    heapq.heappush(q,(43,0))
    heapq.heappush(q,(43,1))
    arr=[]
    while q:
        x=heapq.heappop(q)
        arr.append((x[0],x[1]))
        
    print(arr)
sol()


points = [[3,3],[5,-1],[-2,4]]
k = 2

print(heapq.nsmallest(k,points,key=lambda x: x[0]*x[0]+x[1]*x[1]))

print(heapq.nlargest(k,points,key=lambda x: x[0]*x[0]+x[1]*x[1]))




arr = [3, 45,65,67,34,92,37]
print(arr)
heapq.heapify(arr)
x = heapq.heappop(arr)
print(x)
x = heapq.heappop(arr)
print(x)