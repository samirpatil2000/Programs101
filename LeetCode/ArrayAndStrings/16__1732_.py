def largestAltitude(list_):
    max_=0
    start=0
    for i in list_:
        start+=i
        if(start>max_):
            max_=start
    return max_

gain = [-5,1,5,0,-7]

print(largestAltitude(gain))
