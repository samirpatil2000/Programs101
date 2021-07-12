n=int(input(''))
list=[i for i in range(0,n)]
total_amount=int(input(''))

for i in range(0,n):
    list[i]=int(input())

list.sort()

sum=0
count=0
i=0
while(sum <= total_amount and i<n):
    sum=sum+list[i]
    i=i+1
    count=count+1
    
print(count-1)