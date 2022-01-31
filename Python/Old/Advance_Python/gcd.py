


def gcd(m,n):
    listM =[]
    listN =[]
    list=[]
    for i in range(1,m+1):
        if(m%i==0):
            listM.append(i)
    for j in range(1,n+1):
        if(n%j==0):
            listN.append(j)
    for element in listM:
        if element in listN:
            list.append(element)
    print(list)
    list.sort()
    list.reverse()
    print(list[0])


print(" First Implementation ")
gcd(24,12)
gcd(30,10)
gcd(18,25)
gcd(8,12)
gcd(14,63)



# Its Implementation
def g_c_d(a, b):
    # g = None

    list=[]
    if (a>b):
        g=a
    else:
        g=b

    for i in range(1,g+1):
        if (a%i==0 and b%i==0):
            list.append(i)
    list.sort()
    list.reverse()
    print(list[0])


print(" Second Implementation ")
g_c_d(24,12)
g_c_d(30,10)
g_c_d(18,25)
g_c_d(8,12)
g_c_d(14,63)



# One More Implementation

def gcd_3(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            ans=i
    return (print(ans))  # this is for loop thats why it will run last value

print(" Third Implementation ")
gcd_3(24,12)
gcd_3(30,10)
gcd_3(18,25)
gcd_3(8,12)
gcd_3(14,63)
gcd_3(1400,693)


def lcd(m,n):
    i=min(m,n)

    while i > 0:
        if (m%i)==0 and (n%i)==0 :
           return i
        else:
            i=i-1
        return i

print("Fourth with whileLoop Implementation ")
lcd(24,12)
lcd(30,10)
lcd(18,25)
lcd(8,12)
lcd(14,63)



