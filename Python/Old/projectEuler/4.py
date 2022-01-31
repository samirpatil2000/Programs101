
def palindromic_number(n):
    reverse=0
    temp=n

    while(temp !=0):
        rem=temp%10
        reverse=reverse*10+rem
        temp=temp//10
    if reverse==n:
        return True
    return False

# print(palindromic_number(900009))


largest_palindrome=0
max_product=0
list=[]
for i in range(100,1000):
    for j in range(100,1000):
        product=i*j
        # print(product)
        if palindromic_number(product):
            largest_palindrome=product
            if (product>max_product):
                max_product=product
                list.append(max_product)
            # print(product)

# sorted=list.sort()
#
# print(sorted)

print(list)

print(max_product)

