"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""






def Nosense_method():
    i=20
    smallest_number = 0
    solution = False
    while(solution==False):
        print(i)
        if(i%2==0 and i%3==0 and i%4==0 and i%5==0 and
            i%6==0 and i%7==0 and i%8==0 and i%9==0 and
            i%10==0 and i%11==0 and i%12==0 and i%13==0 and
            i%14==0 and i%15==0 and i%16==0 and i%17==0 and
            i%18==0 and i%19==0 and i%20==0):

            smallest_number=i


            solution=True
            print(smallest_number)
        i += 20

    return smallest_number


# USING continue  statement


def Advance_Method(n):
    for i in range(2,21):
        if n%i==0:
            continue
        else:
            return False
    return True

num=False
answer=20
while(num==False):
    # print(answer)
    num=Advance_Method(answer)
    if num==True:
        print("Answer is true",answer)
    answer+=20


'232792560'
"""
n=20
while not Advance_Method(n):
    print(n)
    n+=20
print(n)"""








