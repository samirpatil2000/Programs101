

def findPowers(powers, n):
    if n == 1:
        return powers[0]
    elif n == 2:
        return powers[1]
    elif n == 3:
        return powers[2]
    else:
        n -= 3
        while n:
            result = powers[0] + powers[1] + powers[2]
            powers = [powers[1], powers[2], result]
            n -= 1
    return powers[-1] % (1e9 + 7)

n = 12
print(findPowers([8, 10, 18], n))



