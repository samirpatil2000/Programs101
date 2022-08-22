

def findPowers(str):
    n = len(str)
    while n - 1:
        str = str[1:] + str[0]
        print(str, end=" ")
        n -= 1
        

findPowers("56743")



