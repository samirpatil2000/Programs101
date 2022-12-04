# a = ["sa", "s2"]
# x = a.copy()
# x[0] = 1
# print(a, x)
# import copy
# x1 = copy.deepcopy(a)
# x1[0] = "d"
# print(x1, a)


def Tuple(tuple, t):
    val = 0
    for tup in tuple:
        if tup == t:
            val += 1
        elif tup < t:
            val += 2
        else:
            return val
    print(tuple)

tuple = (1, 1, 2, 2, 5)

print(Tuple)
print(ord('r'))