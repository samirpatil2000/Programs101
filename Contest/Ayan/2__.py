from collections import Counter
def fun(ids, m):
    count_dict = Counter(ids)
    occurance = sorted(count_dict.values())
    for i in range(len(occurance)):
        if m == 0 or occurance[i] > m:
            return len(occurance[i:])
        else:
            m -= occurance[i]
    

ids = [1, 1, 5, 5]
m = 2

ids = [1, 2, 3, 1, 2, 2, 1]
m = 3
print(fun(ids, m))