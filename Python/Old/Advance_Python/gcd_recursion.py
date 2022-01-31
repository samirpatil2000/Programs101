def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return n
    else:
        diff = m-n
        return (gcd(max(n,diff),min(n,diff)))


print(gcd(24,12))
print(gcd(30,10))
print(gcd(18,25))
print(gcd(8,12))
print(gcd(14,63))

def gcd_1(m,n):
    if m<n:
        (m,n)=(n,m)
    if (m%n)==0:
        return n
    while (m%n !=0):  # if this thing become zero then it will goes out of the loop 
        diff = m-n
        return (gcd_1(max(diff,n),min(diff,n)))


print(gcd_1(24,12))
print(gcd_1(30,10))
print(gcd_1(18,25))
print(gcd_1(8,12))
print(gcd_1(14,63))