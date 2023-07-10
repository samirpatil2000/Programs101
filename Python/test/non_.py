
def checkDigit(n):
    while n > 10:
        n = sum([int(i) for i in str(n)])
    return n

print(checkDigit(55555))
    