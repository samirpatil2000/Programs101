
def method_1(n:int):
    a=set()
    b=set()
    subset_sum=(n*(n+1))//2
    if subset_sum&1==0:
        subset_sum=subset_sum//2
        for i in range(n,0,-1):
            if i<=subset_sum:
                subset_sum-=i
                a.add(i)
            else:
                b.add(i)
        print("YES")
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)
    else:
        print("NO")

n=int(input())
method_1(n)
    